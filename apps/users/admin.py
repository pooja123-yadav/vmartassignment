from django.contrib import admin
from django.contrib import messages
from .models import User


# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone_number','email', 'is_active', 'created')
    list_display_links = ('first_name', 'email')
    ordering = ('-created',)
    actions_on_bottom = False
    actions_on_top = True
    search_fields = ('first_name', 'last_name', 'phone_number', 'email')
    

    def make_active(modeladmin, request, queryset):
        queryset.update(is_active=1)
        messages.success(request, "Selected Record(s) Marked as Active Successfully !!")

    def make_inactive(modeladmin, request, queryset):
        queryset.update(is_active=0)
        messages.success(request, "Selected Record(s) Marked as Inactive Successfully !!")


admin.site.register(User, UserAdmin)

