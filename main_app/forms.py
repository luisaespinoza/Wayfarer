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

class EditForm(UserChangeForm):
  class Meta:
    model = User
    fields = 
  # new fields here

  class Meta(UserChangeForm):
    model = User
    fields = UserChangeForm.Meta.fields + ('new fields here')