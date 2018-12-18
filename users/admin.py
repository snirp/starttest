from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
import pprint
from django.contrib.sessions.models import Session
from django.conf import settings

from .models import User


class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return pprint.pformat(obj.get_decoded()).replace('\n', '<br>\n')
    _session_data.allow_tags=True
    list_display = ['session_key', '_session_data', 'expire_date']
    readonly_fields = ['_session_data']
    exclude = ['session_data']
    date_hierarchy='expire_date'

if settings.ACCOUNT_AUTHENTICATION_METHOD == 'email':
    class UserAdmin(BaseUserAdmin):
        fieldsets = (
            (None, {'fields': ('email', 'password', 'name', 'last_login')}),
            ('Permissions', {'fields': (
                'is_active', 
                'is_staff', 
                'is_superuser', 
                'groups', 
                'user_permissions',
            )}),
        )
        add_fieldsets = (
            (None, {'classes': ('wide',), 'fields': (
                'email', 
                'password1', 
                'password2'
            )}),
        )

        list_display = ('email', 'name', 'is_staff', 'last_login')
        list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
        search_fields = ('email',)
        ordering = ('email',)
        filter_horizontal = ('groups', 'user_permissions',)

else:
    class UserAdmin(BaseUserAdmin):
        fieldsets = (
            (None, {'fields': ('username', 'email', 'password', 'name', 'last_login')}),
            ('Permissions', {'fields': (
                'is_active', 
                'is_staff', 
                'is_superuser', 
                'groups', 
                'user_permissions',
            )}),
        )
        add_fieldsets = (
            (None, {'classes': ('wide',), 'fields': (
                'username',
                'email', 
                'password1', 
                'password2'
            )}),
        )

        list_display = ('username', 'email', 'name', 'is_staff', 'last_login')
        list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
        search_fields = ('username', 'email',)
        ordering = ('username',)
        filter_horizontal = ('groups', 'user_permissions',)    

admin.site.register(User, UserAdmin)
admin.site.register(Session, SessionAdmin)