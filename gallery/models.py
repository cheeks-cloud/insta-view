from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
  photo = models.ImageField(upload_to='images')
  bio = models.TextField()

  def __str__(self):
      return self.bio

class Image(models.Model):
  image = models.ImageField(null=False, blank=False, upload_to='images/')
  name = models.CharField(max_length=40,null=False, blank=False)
  caption = models.TextField(null=False, blank=False)
  profile = models.ForeignKey(User, on_delete = models.CASCADE)
  comments = models.TextField(null=False, blank=False)
  likes = models.IntegerField(null=False, blank=False)


  def save_image(self):
    self.save()

  def delete_image(self):
     Image.objects.get(id = self.id).delete()

  def update_captions(self):
    Image.objects.filter(caption = self.caption).update(caption = self.caption)
  
  @classmethod
  def search_by_name(cls, search_term):
    image = cls.objects.filter(cls,image_name_icontains = search_term)
    return image

  def __str__(self):
      return self.name




