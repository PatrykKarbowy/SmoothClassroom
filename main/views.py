from re import L
from django.shortcuts import render, redirect
from .forms import RegistrationForm, PostForm, TaskForm, ClassroomForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group
from .models import Post, Task, Classroom
from django.contrib import messages

# Create your views here.
@login_required(login_url='/login')
def home(request):
    posts = Post.objects.all()
    if request.method == 'POST':
        post_id = request.POST.get('post-id')
        user_id = request.POST.get('user-id')
        if post_id:
            post = Post.objects.filter(id=post_id).first()
            if post and (post.author == request.user or request.user.has_perm("main.delete_post")):
                post.delete()
        elif user_id:
            user = User.objects.filter(id=user_id).first()
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
@login_required(login_url='/login')
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("/home")
    else:
        form = PostForm()
    return render(request, 'main/create_post.html', {'form': form})

def sign_up(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegistrationForm()
        
    return render(request, 'registration/sign_up.html', {"form": form})


@login_required(login_url = "/login")
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
                return redirect('/create_task')
    form = TaskForm()
    return render(request, 'main/create_task.html', {'form': form, 'tasks': tasks})


@login_required(login_url="/login")
def create_classroom(request):
    if request.method == "POST":
        form = ClassroomForm(request.POST)
        if form.is_valid():
            classroom = form.save(commit=False)
            classroom.save()
            return redirect("/home")
    else:
        form = ClassroomForm()
    return render(request, 'main/create_classroom.html', {"form": form})

def classroom(request, id):
    classroom = Classroom.objects.get(id = id)
    
    return render(request, 'main/classroom.html', {"classroom": classroom})