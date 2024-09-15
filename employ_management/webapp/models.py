from django.db import models
from PIL import Image
from io import BytesIO
from django.core.files import File

class Record(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    photo = models.ImageField(upload_to='photos/')

    def save(self, *args, **kwargs):
        # Resize image before saving
        if self.photo:
            img = Image.open(self.photo)
            output_size = (300, 300)  # You can adjust the size as needed
            img = img.resize(output_size, Image.LANCZOS)

            # Save the resized image to a BytesIO object
            thumb_io = BytesIO()
            img.save(thumb_io, format='JPEG')

            # Use the BytesIO object to create a new Django file object
            self.photo = File(thumb_io, name=self.photo.name)
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.full_name
