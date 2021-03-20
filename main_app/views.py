from django.shortcuts import render ,redirect
from django.contrib.auth import login, get_user_model
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from main_app.forms import SignUpForm, EditUserForm, NewPostForm, EditPostForm
# from django.contrib.auth.models import User
from .models import User,Post,City
# Create your views here.


User = get_user_model()


def home(request):
  cities =City.objects.all()
  posts = Post.objects.all()
  context = {'cities': cities, 'posts': posts}
  return render(request, 'index.html', context)

def user_login(request):
  error_message = ''
  if request.method == 'POST' :
    user = AuthenticationForm(request.POST)
    user = SignUpForm(request.POST)
    print(user)
    login(request, user)
    return redirect('home')
  else:
    return redirect('home')

def post_details(request, post_id):
  post = Post.objects.get(id=post_id)
  post_belongs_to_user = post.author.id == request.user.id 
  post_fields = {'title':post.title, 'content': post.content, 'city': post.city}
  edit_post_form = EditPostForm(initial=post_fields)
  # edit_post_form.fields['city'].widget.attrs['disabled'] = True
  context = {'post': post, 'edit_post_form': edit_post_form ,"post_belongs_to_user": post_belongs_to_user}
  return render(request, 'posts/details.html', context)

@login_required
def new_post(request):
  error_message = ''
  if request.method == 'POST' :
    new_post = NewPostForm(request.POST)
    print('Im posting========================================')
    if new_post.is_valid():
      print('Im valid========================================')
      city= new_post.cleaned_data.get('city')
      content = new_post.cleaned_data.get('content')
      title = new_post.cleaned_data.get('title')
      author = request.user
      create_post =  Post.objects.create(title=title, content=content, city=city, author=author)
      create_post.save()
      return redirect('cities')
    print(new_post.errors)
  else: 
    error_message = 'Invalid post ------------ try again'
  return redirect('cities')

@login_required
def edit_post(request, post_id):
  error_message: ''
  if request.method == 'POST' :
    post = Post.objects.get(id=post_id)
    edit_post = EditPostForm(request.POST, instance=post)
    edit_post.city= post.city
    if edit_post.is_valid():
      edit_post.save()
      # return redirect(f'posts/details/{post_id}')
      return redirect(f'/posts/{post_id}/details')
  else:
    error_message= 'invalid post - try again'
  return redirect('cities')

def delete_post(request, post_id):
  post_to_delete=Post.objects.get(id=post_id)
  post_to_delete.delete()
  return redirect('cities')


def cities_details(request, city_id):
  cities = City.objects.all()
  city = City.objects.get(id=city_id)
  new_post_form= NewPostForm(initial={'city':city})
  context = {'new_post_form': new_post_form, 'cities':cities, 'city':city}
  return render(request, 'cities/index.html', context)

def cities(request):
  city_id=1
  return redirect(f'/cities/{city_id}')


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
      return redirect('profile')
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





