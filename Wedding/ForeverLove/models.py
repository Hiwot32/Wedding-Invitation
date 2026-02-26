from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User

# Wedding main info
class Wedding(models.Model): 
    bride_name = models.CharField(max_length=100, null=True, blank=True)
    groom_name = models.CharField(max_length=100, null=True, blank=True)
    wedding_date = models.DateField( null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    story = models.TextField(null=True, blank=True)
    herStory=models.TextField(null=True, blank=True)
    hisStory=models.TextField(null=True, blank=True)
    how_we_met=models.TextField(null=True, blank=True)
    dateOfMeet=models.DateField(null=True, blank=True)
    first_date=models.TextField(null=True, blank=True)
    dateOfDate=models.DateField(null=True, blank=True)
    proposal=models.TextField(null=True, blank=True)
    dateOfProposal=models.DateField(null=True, blank=True)
    engagement=models.TextField(null=True, blank=True)
    dateOfEngagement=models.DateField(null=True, blank=True)
    marriage=models.TextField(null=True, blank=True)
    

    def __str__(self):
        return self.bride_name
    


# Wedding Images (cover, about, gallery)
class Image(models.Model):
    wedding = models.OneToOneField(Wedding, on_delete=models.CASCADE)
    herImage = models.ImageField(upload_to='images/', null=True, blank=True)
    hisImage = models.ImageField(upload_to='images/', null=True, blank=True)
    meet=models.ImageField(upload_to='images/', null=True, blank=True)
    engagement=models.ImageField(upload_to='images/', null=True, blank=True)
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
        return f"Images for {self.wedding.bride_name}"


# Guest names
class Guest(models.Model):
    wedding = models.ForeignKey(Wedding, on_delete=models.CASCADE)
    guest_name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.guest_name


# RSVP responses + comments
class RSVP(models.Model):
    wedding = models.ForeignKey(Wedding, on_delete=models.CASCADE)
    guest = models.ForeignKey(Guest, on_delete=models.CASCADE)
    attending = models.BooleanField(null=True)
    number_of_guests=models.IntegerField(null=True, blank=True)
    comment=models.TextField(null=True, blank=True)
    responded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.guest.guest_name