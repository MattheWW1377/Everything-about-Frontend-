from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title': 'Главная'
    }
    return render(request, 'index/index.html', context)

def demand(request):
    context = {
        'title': 'Востребованность'
        }
    return render(request, 'index/demand.html', context)

def geography(request):
    context = {
        'title': 'География'
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