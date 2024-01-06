from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('memory/', memory, name='memory'),
    path('login/', login, name='login'),
    path('category/', show_category, name='category'),
    path('category/<int:cat_id>/', show_category_all, name='category'),
]

