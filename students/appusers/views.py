from django.contrib.auth import authenticate, login, logout,get_user_model
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .forms import LoginUserForm, RegisterUserForm,ProfileUserForm,UserPasswordChangeForm
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView,UpdateView


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'appusers/login.html'
    extra_context = {'title': 'Авторизация'}

    # def get_success_url(self):
    #    return reverse_lazy('home')

def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))  # 127.0.0.1:8000
    # return HttpResponseRedirect(reverse('users:login'))  # 127.0.0.1:8000/users/logout  - namespace='users'


# def register(request):
#    form = RegisterUserForm()
#    return render(request,'appusers/register.html',{'form':form})

# def register(request):
#    ''' Ручное регистрация [с помощью функции register() ] '''
#    if request.method == 'POST':
#        form = RegisterUserForm(request.POST)
#        if form.is_valid():
#            user = form.save(commit=False)
#            user.set_password(form.cleaned_data['password'])
#            user.save()
#            # организуем   'appusers/register_done.html'
#            return render(request,'appusers/register_done.html')
#
#    else:
#        form = RegisterUserForm()
#    return render(request,'appusers/register.html',{'form':form})

# вместо def register(request): пишем класс
# from django.views.generic import CreateView

class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'appusers/register.html'
    extra_context = {'title': 'Регистрация'}
    success_url = reverse_lazy('users:login')


class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'appusers/profile.html'
    extra_context = {'title': 'Профиль пользователя'}

    def get_success_url(self):
        #return reverse_lazy('users:profile',args=[self.request.user.pk])
        return reverse_lazy('users:profile')

    def get_object(self,queryset=None):
        return self.request.user


class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy("users:password_change_done")
    template_name = "appusers/password_change_form.html"
