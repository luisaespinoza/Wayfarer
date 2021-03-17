from django.urls import path, include
from . import views


urlpatterns = [
  # path('admin/', a)
  path('', views.home, name='home'),
  path('user_login/', views.user_login, name='user_login'),
  path('accounts/', include('django.contrib.auth.urls')),
  path('accounts/signup', views.signup, name='signup'),
]
