from django.shortcuts import render
from .models import *

# Create your views here.

def home_page(request):
    return render(request, 'homePage.html')

def about_page(request):
    return render(request, 'aboutPage.html')

def story_page(request):
    return render(request, 'story.html')

def galler_page(request):
    return render(request, 'gallery.html')

def couples_info(request):
    if request.method=="POST":
        bride_name = request.POST.get("bride_name")
        groom_name = request.POST.get("groom_name")
        wedding_date = request.POST.get("wedding_date")
        location = request.POST.get("location")
        story = request.POST.get("story")
        herStory = request.POST.get("herStory")
        hisStory = request.POST.get("hisStory")
        how_we_met = request.POST.get("how_we_met")
        first_date = request.POST.get("first_date")
        proposal = request.POST.get("proposal")
        engagement = request.POST.get("engagement")
        marriage = request.POST.get("marriage")

        Wedding.objects.create(
            bride_name=bride_name,
            groom_name=groom_name,
            wedding_date=wedding_date,
            location=location,
            story=story,
            herStory=herStory,
            hisStory=hisStory,
            how_we_met=how_we_met,
            first_date=first_date,
            proposal=proposal,
            engagement=engagement,
            marriage=marriage
        )
        


        


    return render(request, 'couplesInfo.html')
