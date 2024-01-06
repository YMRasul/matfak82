from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, Http404,StreamingHttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from students import settings
from .utils import menu


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')  # должны импортировать эту функцию

def home(request):   #  home   Главная страница
    photomain = PhotoMain.objects.all()[:1] # последно измененый запись
                                        # (Первый QerySet по ordering = ['-time_update']
    cntxt ={
        'photomain': photomain,
        'menu': menu,
        'title': 'ТашГУ матфак82',
    }
    return render(request, 'apprasm/home.html', context=cntxt) #  home   Главная страница

def memory(request):
    return render(request, 'apprasm/about.html', {'menu': menu,'title': 'О сайте'})

def login(request):
    return render(request, 'apprasm/login.html', {'menu': menu,'title': 'Вход'})

def show_category(request):   # список категории и одна(первая) фотография из all
    cats = Categ.objects.all()
    firstphoto = PhotoAll.objects.filter(pk=1)

    #print(f'Категория {cats}')

    if len(firstphoto) == 0:
        raise Http404()

    cntxt = {
            'photo': firstphoto,
            'cats': cats,
            'menu': menu,
            'title': 'ТашГУ матфак82 (альбом)',
    }
    # список категории и одна(первая) фотография из all
    return render(request, 'apprasm/mphoto.html',  context=cntxt)

def show_category_all(request,cat_id):  # Все фотографии категории cat_id
    cats = Categ.objects.all()
    photoall = PhotoAll.objects.filter(cat_id=cat_id)

    #print(f'Категория show_category_all =  {cats}')

    if len(photoall) == 0:
        raise Http404()

    cntxt = {
            'photo': photoall,
            'cats': cats,
            'menu': menu,
            'title': 'ТашГУ матфак82 (альбом)',
            'cat_selected': cat_id,
    }
    return render(request, 'apprasm/mphoto.html', context=cntxt)


def videos(request):
    return render(request, 'photo/about.html', {'menu': menu,'title': 'Видеолар'})

