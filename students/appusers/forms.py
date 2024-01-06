#from django import forms
#class LoginUserForm(forms.Form):
#    username = forms.CharField(label='Логин:',
#                               widget=forms.TextInput(attrs={'class': 'form-input'}))
#    password = forms.CharField(label='Пароль:',
#                               widget=forms.PasswordInput(attrs={'class': 'form-input'}))


from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин:',
                               widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль:',
                               widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    class Meta:
        model = get_user_model()
        fields = ['username','password']

'''
class RegisterUserForm(forms.ModelForm):
    # класс для формы от  forms.ModelForm
    username = forms.CharField(label="Логин")
    password = forms.CharField(label="Пароль",widget=forms.PasswordInput())
    password2= forms.CharField(label="Повтор паролья",widget=forms.PasswordInput())
    class Meta:
        model  = get_user_model()
        fields = ['username','email','first_name','last_name','password','password2']
        labels = { 'email':'E-mail',
                   'first_name':'Имя',
                   'last_name':'Фамилия'
                  }
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Пароли не совпадают")
        return cd['password']
    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует!")
        return email
'''

#from django.contrib.auth.forms import UserCreationForm
class RegisterUserForm(UserCreationForm):
    ''' Регистрация с помощьб класса UserCreationForm  '''
    username = forms.CharField(label="Логин",widget=forms.TextInput(attrs={'class':'form-input'}))
    password1 = forms.CharField(label="Пароль",widget=forms.PasswordInput(attrs={'class':'form-input'}))
    password2 = forms.CharField(label="Повтор паролья",widget=forms.PasswordInput(attrs={'class':'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username','email','first_name','last_name','password1','password2']
        labels = { 'email':'E-mail',
                   'first_name':'Имя',
                   'last_name':'Фамилия'
                  }
    widgets = {
        'email': forms.TextInput(attrs={'class':'form-input'}),
        'first_name': forms.TextInput(attrs={'class': 'form-input'}),
        'last_name': forms.TextInput(attrs={'class': 'form-input'})
    }

    # def clean_password2(self) здесь не нужен потому что
    # стандартные проверки берет на себя класс UserCreationForm
    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Такой E-mail уже существует!")
        return email

# форма для профиля пользователя
class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(disabled=True,label="Логин",widget=forms.TextInput(attrs={'class':'form-input'}))
    email    = forms.CharField(disabled=True,label="E-mail",widget=forms.TextInput(attrs={'class':'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username','email','first_name','last_name']
        labels = {  'first_name':'Имя',
                   'last_name':'Фамилия'
                  }
    widgets = {
        'first_name': forms.TextInput(attrs={'class': 'form-input'}),
        'last_name': forms.TextInput(attrs={'class': 'form-input'})
    }