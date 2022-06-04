from django.db import models

class Profile(models.Model):
  photo = models.ImageField(null=False, blank=False, upload_to='images')
  bio = models.TextField(null=False, blank=False)


  def __str__(self):
      return self.photo

class Image(models.Model):
  image = models.ImageField(null=False, blank=False, upload_to='images/')
  name = models.CharField(max_length=40,null=False, blank=False)
  caption = models.TextField(null=False, blank=False)
  profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
  comments = models.TextField(null=False, blank=False)
  likes = models.IntegerField(null=False, blank=False)


  def save_image(self):
    self.save()

  def delete_image(self):
     Image.objects.get(id = self.id).delete()

  def update_captions(self):



   def __str__(self):
      return self.image




