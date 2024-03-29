from django.shortcuts import render, redirect
from .forms import RegistrationForm, PostForm, TaskForm, ClassroomForm
from django.contrib.auth import login
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User, Group
from .models import Post, Task, Classroom, Message
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.views.generic.list import ListView
from django.db.models import Q


# Create your views here.
def home(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        post_delete = request.POST.get('post_delete')
        ban_user = request.POST.get('ban_user')
        if post_delete:
            post = Post.objects.filter(id=post_delete).first()
            if post and (post.author == request.user or request.user.has_perm("main.delete_post")):
                post.delete()
        elif ban_user:
            user = User.objects.filter(id=ban_user).first()
            if user and request.user.is_staff:
                try:
                    group = Group.objects.get(name='default')
                    group.user_set.remove(user)
                except:
                    pass
                try:
                    group = Group.objects.get(name='mod')
                    group.user_set.remove(user)
                except:
                    pass     
    classrooms = Classroom.objects.all()
    return render(request, 'main/home.html', {"posts": posts, "classrooms":classrooms,})


@permission_required("main.add_post", login_url='/login', raise_exception=True)
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'main/create_post.html', {'form': form})

def update_post(request, id):
    post_detail = Post.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post_detail)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm(instance=post_detail)
    return render(request, 'main/create_post.html', {'form': form})
        

def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Your account has been created')
            return redirect('home')
    else:
        form = RegistrationForm()
        
    return render(request, 'registration/sign_up.html', {"form": form})    

def create_task(request):
    tasks = Task.objects.order_by("id").all()
    if request.method == 'POST':
        task_id_update = request.POST.get('task_id_update')
        task_id_delete = request.POST.get('task_id_delete')
        if task_id_update:
            task = Task.objects.filter(id=task_id_update).first()
            task.finished = not task.finished
            task.save()
        elif task_id_delete:
            task = Task.objects.filter(id=task_id_delete).first()
            task.delete()
        else:
            form = TaskForm(request.POST)
            if form.is_valid():
                task = form.save(commit=False)
                task.author = request.user
                task.save()
                return redirect('create_task')
    form = TaskForm()
    return render(request, 'main/create_task.html', {'form': form, 'tasks': tasks})


def create_classroom(request):
    if request.method == "POST":
        form = ClassroomForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Classroom created successfully')
            return redirect('home')
    else:
        form = ClassroomForm()
    return render(request, 'main/create_classroom.html', {"form": form})

def classroom(request, id):
    classroom = Classroom.objects.get(id = id)
        
    return render(request, 'main/classroom.html', {"classroom": classroom,})

def send_message(request):
    message = request.POST['message']
    student = request.user
    classroom_id = request.POST['classroom_id']
    classroom = Classroom.objects.get(id = classroom_id)
    new_message = Message.objects.create(text=message, author=student, classroom=classroom)
    new_message.save()
    return HttpResponse("Done")

def get_messages(request, id):
    classroom = Classroom.objects.get(id = id)
    messages = Message.objects.filter(classroom = classroom)
    final_messages = list(messages.values())
    i = 0
    for message in messages:
        author = message.author.username
        final_messages[i]["author_name"] = author
        i += 1
    
    return JsonResponse({"messages":final_messages})

class SearchResultsListView(ListView):
    model = Post
    context_object_name = 'post_list'
    template_name = 'main/search_post_results.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Post.objects.filter(
            Q(title__icontains = query) | Q(author__username__icontains = query) | Q(description__icontains = query)
        )
    
