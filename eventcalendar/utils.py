from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Lesson


class Calendar(HTMLCalendar):
    cssclasses_weekday_head=["weekdays" for x in range(8)]
    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()
        # formats a day as a td
        # filter lessons by day
    def formatday(self, day, lessons):
        lessons_per_day = lessons.filter(start_time__day=day)
        d = ''
        for lesson in lessons_per_day:
            start_time = lesson.start_time
            end_time = lesson.end_time
            lesson_time = f'{start_time.strftime("%H:%M")} - {end_time.strftime("%H:%M")}'
            d += f'<div class="event-title">/{lesson.subject.name}</div><div class="event-desc">{lesson.description} </div><div class="event-time">{lesson_time}</div>'

        if day != 0 and lessons_per_day:
            return f"<td class='day'><span class='date'>{day}</span><div class='event'>{d}</div></td>"
        elif day == 0:
            return f"<td class='day other-month'</td>"
        else:
            return  f"<td class='day'><span class='date'>{day}</span></td>"

        # formats a week as a tr 
    def formatweek(self, theweek, lessons):
        week = ''
        for d, weekday in theweek:
            week += self.formatday(d, lessons)
        return f'<tr class="days"> {week} </tr>'

    # formats a month as a table
    # filter lessons by year and month
    def formatmonth(self, withyear=True):
        lessons = Lesson.objects.filter(start_time__year=self.year, start_time__month=self.month)
        cal = f'<table id="calendar">\n'
        cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
        cal += f'{self.formatweekheader()}\n'
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f'{self.formatweek(week, lessons)}\n'
        return cal