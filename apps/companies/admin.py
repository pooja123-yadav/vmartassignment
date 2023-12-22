from django.contrib import admin
from django.contrib import messages
from .models import Company

# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'industry', 'founded_date', 'is_active', 'created')
    list_display_links = ('name', 'industry')
    ordering = ('-created',)
    actions_on_bottom = False
    actions_on_top = True
    search_fields = ('name', 'industry', 'founded_date', 'description')
    

    def make_active(modeladmin, request, queryset):
        queryset.update(is_active=1)
        messages.success(request, "Selected Record(s) Marked as Active Successfully !!")

    def make_inactive(modeladmin, request, queryset):
        queryset.update(is_active=0)
        messages.success(request, "Selected Record(s) Marked as Inactive Successfully !!")


admin.site.register(Company, CompanyAdmin)
