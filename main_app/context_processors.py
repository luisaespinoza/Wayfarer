from main_app.forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm

def signup_and_login_forms(request):
  return {
    'login_form' : AuthenticationForm(), 'signup_form': SignUpForm()
  }