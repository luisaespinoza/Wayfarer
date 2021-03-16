from django.urls import path, include
from . import views


urlpatterns = [
  # path('admin/', a)
  path('', views.home, name='home'),
  path('accounts/', include('django.contrib.auth.urls')),
  path('accounts/signup', views.signup, name='signup'),
  path('accounts/profile/', views.profile, name='profile'),
]
