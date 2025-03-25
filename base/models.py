from django.db import models

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['-updated', '-created']
    

class Location(models.Model):
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.address[0:50]
    

class Contact(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200, null=True, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.str('name')


