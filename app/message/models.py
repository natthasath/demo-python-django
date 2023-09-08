from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField 

# Create your models here.
class msg(models.Model):
    title = models.CharField(max_length=30)
    subject = models.CharField(max_length=50)
    # body = models.TextField()
    body = RichTextUploadingField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Message'

    def __str__(self) :
        return self.title