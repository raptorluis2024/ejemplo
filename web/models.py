from django.db import models
import uuid

# Create your models here.
class Flan(models.Model):
    flan_uuid = models.UUIDField( 
         primary_key = True, 
         default = uuid.uuid4, 
         editable = False) 
    name = models.CharField(max_length=64)
    description = models.TextField()
    image_url = models.URLField()
    slug = models.SlugField()
    is_private = models.BooleanField()

    def __str__(self):
        return self.name