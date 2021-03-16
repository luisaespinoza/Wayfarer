from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from main_app.forms import SignUpForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
  form =SignUpForm()
  return render(request, "index.html", {'form' :form})


def signup(request):
  error_message =''
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
  else:
    error_message = 'Invalid sign up - try again'
  form = SignUpForm()
  context = {'form':form, 'error_message':error_message}
  return(request, 'registration/signup.html')