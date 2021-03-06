from django.urls import path, include
from . import views


urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('posts/new', views.new_post, name='new_post'),
  path('posts/<int:post_id>/edit', views.edit_post, name='edit_post'),
  path('posts/<int:post_id>/details/', views.post_details, name='post_details'),
  path('posts/<int:post_id>/delete' , views.delete_post, name='delete_post'),
  path('accounts/', include('django.contrib.auth.urls')),
  path('cities/', views.cities, name='cities'),
  path('cities/<int:city_id>', views.cities_details, name='cities_details'),
  path('accounts/signup', views.signup, name='signup'),
  path('accounts/profile/', views.profile, name='profile'),
  path('accounts/profile_edit/', views.profile_edit, name='profile_edit'),
]