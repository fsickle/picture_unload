from django.db import models
from datetime import date
from django.urls import reverse

class IMG(models.Model):
    img = models.ImageField(upload_to='img')
    name = models.CharField(max_length=20)
    date_added = models.DateTimeField(default=date.today)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('picture_unloads:show',args=[str(self.id)])
    

