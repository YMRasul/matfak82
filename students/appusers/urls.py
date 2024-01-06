from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

app_name = 'users'

#urlpatterns = [
#    path('login/', login_user, name='login'),
#    path('logout/', logout_user, name='logout'),
#]

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    #path('logout/', logout_user, name='logout'),
    path('logout/', LogoutView.as_view(), name='logout'),
    #path('register/', register, name='register'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('profile/', ProfileUser.as_view(), name='profile'),
]


# path('logout/', LogoutView.as_view(), name='logout'),

# для LogoutView
#<form action="{% url 'appusers:logout' %}" method="post">
#    {% csrf_token %}
#    <button type="submit">Выход</button>
#</form>
