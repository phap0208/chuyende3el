from django.contrib import admin
from .models import Course, Lesson, Test, Question,Profile

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Test)
admin.site.register(Question)
admin.site.register(Profile)
