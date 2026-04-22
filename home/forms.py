from django import forms
from home.models import Task

class Taskform(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'content', 'user']
        
