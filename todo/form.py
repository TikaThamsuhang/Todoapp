from django import forms
from .models import todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = todo
        fields = ['todo_name'] 
