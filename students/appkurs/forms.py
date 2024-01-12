from django import forms
from .models import Student,Group


class UpdateStudentForm(forms.ModelForm):
    grp = forms.ModelChoiceField(queryset=Group.objects.all(),empty_label="Группа не выбрана",label="Группа")

    class Meta:
        model = Student
        fields = ['title', 'grp', 'content', 'birthday', 'photo','is_live']
        widgets = {
                    'title': forms.TextInput(attrs={'class': 'form-input'}),
                    'content': forms.Textarea(attrs={'cols':50,'rows':5})
                  }