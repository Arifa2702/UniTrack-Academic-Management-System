from django.contrib import admin
from .models import Student, Course, Result, Attendance

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Result)
admin.site.register(Attendance)