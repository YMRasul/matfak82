from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseNotFound, Http404,StreamingHttpResponse
from django.shortcuts import render, redirect,get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from .forms import UpdateStudentForm
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

def show_student(request,student_id):
    grps = Group.objects.all()
    student = Student.objects.get(pk=student_id)

    #print(f"{student=}")
    #if len(student) == 0:
    #    raise Http404()

    cntxt = {
            'grps': grps,
            'photo': student,
            'menu': menu,
            'title': 'ТашГУ матфак82',
            'cat_selected': None,
    }
    return render(request, 'appkurs/student.html', context=cntxt)


def edit_student(request,student_id):
    return HttpResponse(f"Отображени с id= {student_id}")


class UpdateStudent(UpdateView):
    model = Student
    form_class = UpdateStudentForm
    #fields = ['title','grp','content','birthday','photo','is_live']
    template_name = 'appkurs/update_student.html'
    #success_url = reverse_lazy('student',args=[1])
    extra_context = {
        'menu':menu,
        'title':'Редактирование'
    }
    # Переопределение  success_url
    def get_success_url(self):
        return reverse_lazy('student', kwargs={'student_id': self.object.pk})
