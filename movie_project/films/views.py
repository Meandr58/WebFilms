from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Films_post
from .forms import Films_postForm

def index(request):
    return render(request, 'films/index.html')

def show(request):
    films = Films_post.objects.all()  # Правильная переменная для фильмов
    return render(request, 'films/show.html', {'films': films})  # Передаем список фильмов в шаблон

def create(request):
    if request.method == 'POST':
        form = Films_postForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')  # Перенаправление после успешного сохранения
        else:
            # Печать ошибок формы для отладки
            print(form.errors)
            error = "Данные были заполнены некорректно"
    else:
        form = Films_postForm()
        error = None  # Инициализация переменной error для GET-запроса

    return render(request, 'films/create.html', {'form': form, 'error': error})







