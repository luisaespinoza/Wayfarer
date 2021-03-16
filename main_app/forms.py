from django.import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class UserCreationForm(UserChangeForm):
  class Meta:
    model = UserChangeForm
    fields = ["username", "email", "city"]


