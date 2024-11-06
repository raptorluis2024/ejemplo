from django.contrib import admin
from .models import Flan


#admin.site.register(Flan)
# Register your models here.
@admin.register(Flan)
class FlanAdmin(admin.ModelAdmin):
    list_display = ('name','description','is_private')
    list_display_links = ('name',)
    search_fields = ('name','description')
    list_per_page = 2
