from django.shortcuts import render ,redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from main_app.forms import SignUpForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
  sign_up_form =SignUpForm()
  login_form = AuthenticationForm
  return render(request, "index.html", {'sign_up_form' :sign_up_form, 'login_form': login_form()})

# def user_login(request):
#   error_message = ''
#   if request.method == 'POST':
#     # user = AuthenticationForm
#     user = SignUpForm(request.POST)
#     print(user)
#     login(request,user)
#     return redirect('home')


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
  context = {'form':form, 'error_message':error_message}
  return render(request, 'index.html', {'form': form})