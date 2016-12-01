from django.db import models

# Create your models here.

class Photo(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(max_length=200, blank=True)
    author = models.ForeignKey('member.MyUser')
    modified_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='photo/photo', blank=False)
    post = models.ForeignKey('photo.Photo')


    def __str__(self):
        return self.title
