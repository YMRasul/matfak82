from django.urls import path

from django.contrib.auth.views\
    import LogoutView,PasswordChangeView,\
    PasswordChangeDoneView,PasswordResetView,PasswordResetDoneView,PasswordResetCompleteView,PasswordResetConfirmView
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

    #Стандартная форма
    #path('password-change/',PasswordChangeView.as_view(),name="password_change"), # Стандартный класс

    path('password-change/',UserPasswordChange.as_view(),name="password_change"),  #  через свой класс
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name="appusers/password_change_done.html"),
                                                                 name="password_change_done"),
    #
    path('password-reset/', PasswordResetView.as_view(
                                       template_name="appusers/password_reset_form.html",
                                       email_template_name="appusers/password_reset_email.html",
                                       success_url=reverse_lazy("users:password_reset_done")
                            ),  name="password_reset"),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name="appusers/password_reset_done.html"),
         name="password_reset_done"),

    path('password-reset/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
                                          template_name="appusers/password_reset_confirm.html",
                                          success_url=reverse_lazy("users:password_reset_complete")
                                          ),name="password_reset_confirm"),

    path('password-reset/complete/',
         PasswordResetCompleteView.as_view(template_name="appusers/password_reset_complete.html"),
         name="password_reset_complete"),

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
