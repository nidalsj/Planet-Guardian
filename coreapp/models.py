from django.db import models

# Create your models here.

class Gallery(models.Model):
    title=models.CharField(max_length=100)
    img=models.ImageField(upload_to='gallery')
    timeStamp=models.DateTimeField(auto_now_add=True,blank=True)
    def __int__(self):
        return self.id
    
class Contact(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField(default='')
    subject=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.email
    

class BlogPost(models.Model):
    CATEGORY_CHOICES = [
        ('biodegradable', 'Biodegradable Waste'),
        ('non_biodegradable', 'Non-Biodegradable Waste'),
        ('hazardous', 'Hazardous Waste'),
        ('recycling', 'Recycling Insights'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=200)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True,blank=True)

    def __str__(self):
        return self.title
    
