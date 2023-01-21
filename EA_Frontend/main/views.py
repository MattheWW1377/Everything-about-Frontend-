from django.shortcuts import render

from main.models import Vos, Main, Geo


def index(request):
    pic = Main.objects.all()
    context = {
        'title': 'Главная',
        'pic': pic
    }
    return render(request, 'index/index.html', context)

def demand(request):
    pic = Vos.objects.all()
    context = {
        'title': 'Востребованность',
        'pic': pic
        }
    return render(request, 'index/demand.html', context)

def geography(request):
    pic = Geo.objects.all()
    context = {
        'title': 'География',
        'pic': pic
    }
    return render(request, 'index/geography.html', context)

def skills(request):
    context = {
        'title': 'Навыки'
    }
    return render(request, 'index/skills.html', context)

def recent_vacancies(request):
    context = {
        'title': 'Последние вакансии'
    }
    return render(request, 'index/recent-vacancies.html', context)