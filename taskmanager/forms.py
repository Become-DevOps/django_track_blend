from django import forms 
from taskmanager.models import Tasks

class taskForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = "__all__" 
        
class editForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ['assigned_to','review','priority']