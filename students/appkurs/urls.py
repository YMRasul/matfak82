from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('group/', show_group, name='group'),
    path('group/<int:grp_id>/', show_group_all, name='group'),
    path('student/<int:student_id>/', show_student, name='student'),
    path('edit/<int:pk>/', UpdateStudent.as_view(), name='edit_student'),
]


