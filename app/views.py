import os

from django.http import HttpResponse
from django.shortcuts import render, reverse
import datetime


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # обратите внимание – здесь HTML шаблона нет,
    # возвращается просто текст
    current_time = datetime.datetime.now().strftime("%H : %M")
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    msg = ''
    dirname = os.listdir(os.getcwd())  # Список содержимого текущего каталога
    for i in dirname:
        out = f'* {i}<br>'
        msg += out

    if not msg:
        raise NotImplemented
    else:
        return HttpResponse(msg)

