from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse
from .models import Lesson
from .forms import AdminLessonForm, LessonForm
from django.views import generic
from .utils import Calendar
from django.utils.safestring import mark_safe
import calendar

class CalendarView(generic.ListView):
    model = Lesson
    template_name = 'calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('month', None))
        cal = Calendar(d.year, d.month, self.request)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(request_month):
    if request_month:
        year, month = (int(x) for x in request_month.split('-'))
        return datetime(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month
    
class LessonCreateView(generic.CreateView):
    model = Lesson
    template_name = 'calendar_add_lesson.html'
    success_url = '/calendar'
    
    def get_form_class(self):
        if self.request.user.is_staff:
            form_class=AdminLessonForm
        else:
            form_class=LessonForm
        return form_class
    
    def form_valid(self, form):
        if self.get_form_class() == LessonForm:
            form.instance.student = self.request.user
        return super().form_valid(form)
    
class LessonUpdateView(generic.UpdateView):
    model = Lesson
    template_name = 'calendar_add_lesson.html'
    success_url = '/calendar'
    
    def get_form_class(self):
        if self.request.user.is_staff:
            form_class=AdminLessonForm
        else:
            form_class=LessonForm
        return form_class
    
    def form_valid(self, form):
        if self.get_form_class() == LessonForm:
            form.instance.student = self.request.user
        form.instance.accepted = False
        return super().form_valid(form)

class LessonDeleteView(generic.DeleteView):
    model = Lesson
    template_name = 'calendar_delete_lesson.html'
    success_url = '/calendar'

class LessonAcceptView(generic.UpdateView):
    model = Lesson
    template_name = 'calendar_accept_lesson.html'
    fields=['accepted']
    success_url = '/calendar'
    
    def form_valid(self, form):
        form.instance.accepted = True
        return super().form_valid(form)