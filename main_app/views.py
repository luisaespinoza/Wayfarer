from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from main_app.forms import SignUpForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
  form = SignUpForm()
  # form2 = LoginForm()
  return render(request, "index.html", {'form' :form })




def signup(request):
  error_message =''
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
  else:
    error_message = 'Invalid sign up - try again'
  form = SignUpForm()
  return render(request, 'registration/signup.html')