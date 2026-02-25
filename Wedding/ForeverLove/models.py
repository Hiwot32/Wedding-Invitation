from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

# Wedding main info
class Wedding(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)  
    bride_name = models.CharField(max_length=100)
    groom_name = models.CharField(max_length=100)
    wedding_date = models.DateField()
    location = models.CharField(max_length=200)
    story = models.TextField()
    herStory=models.TextField()
    hisStory=models.TextField()
    how_we_met=models.TextField()
    first_date=models.TextField()
    proposal=models.TextField()
    engagement=models.TextField()
    marriage=models.TextField()

    def __str__(self):
        return self.bride_name
    


# Wedding Images (cover, about, gallery)
class Image(models.Model):
    wedding = models.OneToOneField(Wedding, on_delete=models.CASCADE)
    CoverImage = models.ImageField(upload_to='images/', null=True, blank=True)
    herImage = models.ImageField(upload_to='images/', null=True, blank=True)
    hisImage = models.ImageField(upload_to='images/', null=True, blank=True)
    meet=models.ImageField(upload_to='images/', null=True, blank=True)
    engaement=models.ImageField(upload_to='images/', null=True, blank=True)
    first_date=models.ImageField(upload_to='images/', null=True, blank=True)
    proposal=models.ImageField(upload_to='images/', null=True, blank=True)
    marriage=models.ImageField(upload_to='images/', null=True, blank=True)
    gallery1 = models.ImageField(upload_to='images/', null=True, blank=True)
    gallery2 = models.ImageField(upload_to='images/', null=True, blank=True)
    gallery3 = models.ImageField(upload_to='images/', null=True, blank=True)
    gallery4 = models.ImageField(upload_to='images/', null=True, blank=True)
    gallery5 = models.ImageField(upload_to='images/', null=True, blank=True)
    gallery6 = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.wedding


# Guest names
class Guest(models.Model):
    wedding = models.ForeignKey(Wedding, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=100)

    def __str__(self):
        return self.guest_name


# RSVP responses + comments
class RSVP(models.Model):
    wedding = models.ForeignKey(Wedding, on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    attending = models.BooleanField()
    numberofGuste=models.IntegerField()
    comment = models.TextField(blank=True)
    responded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.guest.guest_name