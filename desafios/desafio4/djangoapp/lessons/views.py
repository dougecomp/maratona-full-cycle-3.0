from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from lessons.models import Lesson

def index(request):
    lessons = Lesson.objects.all()
    template = loader.get_template('lessons/index.html')
    context = {
        'lessons': lessons
    }
    return HttpResponse(template.render(context, request))