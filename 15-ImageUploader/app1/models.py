from django.db import models

# Create your models here.


class ImageCollectionModel(models.Model):
    image_name = models.CharField(max_length=200)
    image_description = models.TextField()
    
    image_time = models.DateTimeField(auto_now_add=True)
    image_file = models.ImageField(upload_to='uploaded_images/')
    
    
    def __str__(self):
        return self.image_name
    