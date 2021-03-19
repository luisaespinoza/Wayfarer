from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Post, City 
from django.contrib.auth.forms import UserChangeForm
# Register your models here.


# class MyUserChangeForm(UserChangeForm):
#   class Meta(UserChangeForm.Meta):
#     model: User

# class UserAdmin(UserAdmin):
#   form: UserChangeForm
#   add_fieldsets = UserAdmin.add_fieldsets + (
#     ('city', {'fields': ('city')}),
#   )
#   fieldsets = UserAdmin.fieldsets + (
#     ('city', {'fields': ['city']}),
#   )

admin.site.register(User, UserAdmin)
admin.site.register(Post)
admin.site.register(City)
