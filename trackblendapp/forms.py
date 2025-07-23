from django import forms
from trackblendapp.models import userdetails 
from django.contrib.auth.models import User 
from django_recaptcha.fields import ReCaptchaField

class userForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User 
        fields = ['username','email','password']
        
class userprofileForm(forms.ModelForm):
    class Meta:
        model = userdetails
        fields = ['phone','address','user_img']
    captcha = ReCaptchaField()