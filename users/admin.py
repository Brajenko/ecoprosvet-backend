from django.contrib import admin

from .models import CustomUser

from django.contrib import admin
from .models import CustomUser
from organizations.models import Organization


class OrganizationInline(admin.StackedInline):
    model = Organization
    can_delete = False
    verbose_name_plural = 'organizations'


class CustomUserAdmin(admin.ModelAdmin):
    inlines = (OrganizationInline, )
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
