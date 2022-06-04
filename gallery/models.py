from django.db import models

class Profile(models.Model):
  photo = models.ImageField(null=False, blank=False, upload_to='images')
  bio = models.TextField(null=False, blank=False)


class Image(models.Model):
  image = models.ImageField(null=False, blank=False, upload_to='images/')
  name = models.CharField(max_length=40,null=False, blank=False)
  caption = models.TextField(null=False, blank=False)
  profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
  comments = models.TextField(null=False, blank=False)
  likes = models.IntegerField(null=False, blank=False)




