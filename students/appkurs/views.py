from django.contrib.auth.decorators import login_required
#from django.http import HttpResponse, HttpResponseNotFound, Http404,StreamingHttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from apprasm.utils import menu

#@login_required(login_url='/admin/') если так это работает до settings.py-> LOGIN_URL = 'users:login'
@login_required
def show_group(request):   # список категории и одна(первая) фотография из all

    grps = Group.objects.all()
    students = Student.objects.all()

    if len(students) == 0:
        raise Http404()

    cntxt = {
            'grps': grps,
            'photo': students,
            'menu': menu,
            'title': 'ТашГУ матфак82 (Однакурсники)',
            'cat_selected': 0
    }
    # список категории и одна(первая) фотография из all
    return render(request, 'appkurs/kurs.html',  context=cntxt)

@login_required
def show_group_all(request,grp_id):
    grps = Group.objects.all()
    studentgroups = Student.objects.filter(grp_id=grp_id)

    if len(studentgroups) == 0:
        raise Http404()

    cntxt = {
            'grps': grps,
            'photo': studentgroups,
            'menu': menu,
            'title': 'ТашГУ матфак82 (Группа)',
            'cat_selected': grp_id,
    }
    return render(request, 'appkurs/kurs.html', context=cntxt)
