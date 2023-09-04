from django.db import models

# Create your models here.
class article(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    publish = models.DateTimeField('publish')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True)

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

    def __str__(self) :
        return self.title
    
    def cutbody(self) :
        return self.body[:255]+"..."