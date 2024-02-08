from django.db import models

# Create your models here.
class Course(models.Model):
    image = models.ImageField(upload_to='media')
    fees = models.IntegerField()
    name = models.CharField(max_length=255)
    facuality = models.CharField(max_length=255)
    duration = models.CharField(max_length=10)
    seat = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
class Team(models.Model):
    image = models.ImageField(upload_to='media')
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Testimonial(models.Model):
    image = models.ImageField(upload_to='media')
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    review = models.TextField()

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name