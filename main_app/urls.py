from django.urls import path, include
from . import views


urlpatterns = [
  # path('admin/', a)
  path('', views.home, name='home'),
  path('post/new', views.new_post, name='new_post'),
  path('post/<int:post_id>/edit', views.edit_post, name='edit_post'),
  path('post/<int:post_id>/details/', views.post_details, name='post_details'),
  path('post/<int:post_id>/delete' , views.delete_post, name='delete_post'),
  # path('user_login/', views.user_login, name='user_login'),
  path('accounts/', include('django.contrib.auth.urls')),
  path('cities/', views.cities, name="cities"),
  path('accounts/signup', views.signup, name='signup'),
  path('accounts/profile/', views.profile, name='profile'),
  path('accounts/profile_edit/', views.profile_edit, name='profile_edit'),

]
