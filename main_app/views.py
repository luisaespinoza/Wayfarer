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



def profile_edit(request):
  error_message =''
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      print("form valid")
      user = form.save()
      print("saved??")
      login(request, user)
      print("logged in?")
      return redirect('home')
  else:
    error_message = 'Invalid sign up - try again'
  form = SignUpForm()
  context = {'form':form, 'error_message':error_message}
  
  return render(request, 'index.html', {'form': form})


def profile(request):
  form = SignUpForm()
  return render(request, "accounts/profile.html", { "form": form })


#  @login_required
# def user_edit(request, user_id):
#   # get a reference to a user
#   user = user.objects.get(id=user_id)
#   # build a form for the user filling it with values from the instance or values from the POST request
#   user_form = userForm(request.POST or None, instance=user)
#   if request.POST and user_form.is_valid():
#     # save changes to the user
#     user_form.save()
#     # redirect to the detail page
#     return redirect('detail', user_id=user_id)
#   else:
#     return render(request, 'users/edit.html', { 'user': user, 'user_form': user_form }) 






