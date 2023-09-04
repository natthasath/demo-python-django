from django.contrib import admin
from .models import article
from import_export.admin import ImportExportModelAdmin

class ArticleAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('title', 'date_created', 'date_updated')
    search_fields = ['title']

# Register your models here.
admin.site.register(article, ArticleAdmin)