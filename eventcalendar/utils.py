from datetime import datetime, timedelta
from calendar import HTMLCalendar, day_name
from .models import Lesson


class Calendar(HTMLCalendar):
    cssclasses_weekday_head=["weekdays" for x in range(8)]
    def __init__(self, year=None, month=None, request=None):
        self.year = year
        self.month = month
        self.request = request
        super(Calendar, self).__init__()
        
        # formats a day as a td
        # filter lessons by day
    def formatday(self, day, lessons):
        lessons_per_day = lessons.filter(start_time__day=day)
        d = ''
        lesson_accepted = False
        for lesson in lessons_per_day:
            if lesson.student.username == self.request.user.username or self.request.user.is_staff:
                lesson_id = lesson.id
                lesson_accepted = lesson.accepted
                edit_button = f'<a class="link-info" href="edit_lesson/{lesson_id}">Change</a>'
                delete_button = f'<a class="link-danger" href="delete_lesson/{lesson_id}">Delete</a>'
                accept_button = f'<a class="btn btn-success" href="accept_lesson/{lesson_id}">Accept</a>'
                start_time = lesson.start_time
                end_time = lesson.end_time
                lesson_time = f'{start_time.strftime("%H:%M")} - {end_time.strftime("%H:%M")}'
                if lesson_accepted:
                    d += f'<div class="event-title">{lesson.subject.name}</div><div class="event-desc">{lesson.description} </div><div class="event-time">{lesson_time}</div>'
                else:
                    d += f'<div class="event-title">{lesson.subject.name}</div><div class="event-desc">{lesson.description} </div><div class="event-time"><b>Wait for acceptation!</b></div>'
            else:
                return f"<td class='day'><span class='date'>{day}</span></td>"
        if self.request.user.is_staff and not lesson_accepted:
            if day != 0 and lessons_per_day:
                return f"<td class='day'><span class='date'>{day}</span>{accept_button}<div class='event'>{d}</div><div class='d-flex justify-content-center'>{edit_button} &nbsp|&nbsp {delete_button}</div></td>"
        else:
            if day != 0 and lessons_per_day:
                return f"<td class='day'><span class='date'>{day}</span><div class='event'>{d}</div><div class='d-flex justify-content-center'>{edit_button} &nbsp|&nbsp {delete_button}</div></td>"            
        if day == 0:
            return f"<td class='day other-month'</td>"
        else:
            return  f"<td class='day'><span class='date'>{day}</span></td>"

        # formats a week as a tr 
    def formatweek(self, theweek, lessons):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, lessons)
        return f'<tr class="days"> {week} </tr>'
    
    def formatweekday(self, day):
        return f'<th class="{self.cssclasses_weekday_head[day]}">{day_name[day]}</th>'

    # formats a month as a table
    # filter lessons by year and month
    def formatmonth(self, withyear=True):
        lessons = Lesson.objects.filter(start_time__year=self.year, start_time__month=self.month)
        cal = f'<div class="d-flex justify-content-center"><h1>{self.formatmonthname(self.year, self.month, withyear=withyear)}</h1></div>\n'
        cal += f'<table id="calendar">\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, lessons)}\n'
        return cal