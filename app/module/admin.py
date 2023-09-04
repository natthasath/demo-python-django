from django.contrib import admin
from .models import article
from import_export.admin import ImportExportModelAdmin

class ArticleAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('title', 'date_created', 'date_updated')
    list_per_page = 1
    search_fields = ['title']
    prepopulated_fields = {'slug': ('title',)} 

# Register your models here.
admin.site.register(article, ArticleAdmin)