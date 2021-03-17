from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class SignUpForm(UserCreationForm):
    email=forms.EmailField(max_length=64)
    username = forms.CharField()
    first_name = forms.CharField(max_length=32)
    last_name=forms.CharField(max_length=32)
    city = forms.CharField(max_length=64)
    
    class Meta(UserCreationForm.Meta):
      model = User
      fields = UserCreationForm.Meta.fields + ('email','first_name','last_name','city')

class EditUserForm(forms.ModelForm):
    class Meta(UserChangeForm.Meta):
      model = User
      fields = ('email','username','first_name','last_name','city')
