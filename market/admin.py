from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import UserCreationForm, UserChangeForm
from .models import *


#
# class CustomUserAdmin(UserAdmin):
#    add_form = UserCreationForm
#    form = UserChangeForm
#    model = User
#    list_display = ['username', 'email', 'user_cell_phone', 'is_buyer', 'is_seller', 'is_staff']
#
# admin.site.register(User, CustomUserAdmin)
#
#
# class ProduceAdmin(admin.ModelAdmin):
#    model = Produce
#    list_display = ['produce', 'price', 'description', 'qty', 'created', 'updated']

admin.site.register(Produce)
admin.site.register(User)



