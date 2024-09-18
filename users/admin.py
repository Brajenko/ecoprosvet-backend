from django.contrib import admin

from .models import CustomUser

from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_staff', 'is_active', 'is_organizer')
    search_fields = ('email', 'organization_name')
    list_filter = ('is_staff', 'is_active', 'is_organizer')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('birthday',)}),
        ('Organization info', {'fields': ('is_organizer', 'organization_name', 'organization_description', 'organization_inn')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_organizer', 'organization_name', 'organization_description', 'organization_inn', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)