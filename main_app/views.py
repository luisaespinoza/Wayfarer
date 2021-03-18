from django.shortcuts import render ,redirect
from django.contrib.auth import login, get_user_model
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from main_app.forms import SignUpForm, EditUserForm
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User
from .models import User,Post,City
# Create your views here.


User = get_user_model()


def home(request):
  sign_up_form =SignUpForm()
  login_form = AuthenticationForm
  context = {'sign_up_form' :sign_up_form, 'login_form': login_form()}
  return render(request, 'index.html', context)

def user_login(request):
  error_message = ''
  if request.method == 'POST' :
    user = AuthenticationForm(request.POST)
    user = SignUpForm(request.POST)
    print(user)
    login(request, user)
    return redirect('home')

def post_details(request, post_id):
  user = get_user_model().objects.get(username=request.user)
  post = Post.objects.get(id=post_id)
  context = {'user': user, 'post': post}
  return render(request, "detail.html", context)

def cities(request):
  return render(request, "cities.html")


def signup(request):
  error_message = ''
  if request.method == 'POST' :
    form = SignUpForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
  else:
    error_message = 'Invalid sign up - try again'
  form = SignUpForm()
  context = {'form':form, 'error_message':error_message}
  return render(request, 'index.html', context)


@login_required
def profile_edit(request):
  error_message =''
  if request.method == 'POST':
    form = EditUserForm(request.POST, instance=request.user)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
  else:
    error_message = 'Invalid sign up - try again'
  form = SignUpForm()
  context = {'form':form, 'error_message':error_message}
  return render(request, 'index.html', context)
  

@login_required
def profile(request):
  print(request)
  user = get_user_model().objects.get(username=request.user)
  user_fields= {'city': user.city, 'email':user.email, 'first_name': user.first_name, 'last_name':user.last_name,'city':user.city , 'username':user.username}
  form = EditUserForm(initial=user_fields)
  context = {'form': form, 'user': user}
  return render(request, 'accounts/profile.html', context)





