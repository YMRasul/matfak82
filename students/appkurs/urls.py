from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('group/', show_group, name='group'),
    path('group/<int:grp_id>/', show_group_all, name='group'),
]


