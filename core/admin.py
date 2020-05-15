from django.contrib.auth.admin import UserAdmin
from django.contrib import admin 

from .forms import UserCreationForm, UserChangeForm
from .models import MyUserAdmin

@admin.register(MyUserAdmin)
class CustomUsuarioAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = MyUserAdmin

    list_display = ('first_name', 'last_name', 'email', 'dt_expiracao', 'is_staff')
    fields_set = (
        (None, {'fields': ('email', 'password')}),
        ('Informações pessoais', {'fields': ('first_name', 'last_name', 'dt_expiracao')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permission')}),
        ('Datas importantes', {'fields': ('last_login', 'date_joined')}),
    )
