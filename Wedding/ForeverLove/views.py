from django.shortcuts import render,redirect
from .models import *

# Create your views here.
w = Wedding.objects.last()
i = Image.objects.get(wedding=w)
print(i.herImage.path) 

def home_page(request):
    weddings = Wedding.objects.last()           # get the latest wedding
    img_obj = Image.objects.filter(wedding=weddings).first()  # get images for that wedding
    context = {
        'weddings': weddings,
        'img_obj': img_obj
    }
    return render(request, 'homePage.html', context)

def about_page(request):
    weddings = Wedding.objects.last() 
    img = Image.objects.filter(wedding=weddings).first()
    return render(request, 'aboutPage.html', {'weddings':weddings, 'img':img})

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

        wedding=Wedding.objects.create(
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
             # Create Image object linked to this wedding
        img_obj = Image(wedding=wedding)

# Assign each uploaded file individually
        img_obj.CoverImage = request.FILES.get("CoverImage")
        img_obj.herImage = request.FILES.get("herImage")
        img_obj.hisImage = request.FILES.get("hisImage")
        img_obj.meet = request.FILES.get("meet")
        img_obj.engaement = request.FILES.get("engaement")
        img_obj.first_date = request.FILES.get("first_date")
        img_obj.proposal = request.FILES.get("proposal")
        img_obj.marriage = request.FILES.get("marriage")
        img_obj.gallery1 = request.FILES.get("gallery1")
        img_obj.gallery2 = request.FILES.get("gallery2")
        img_obj.gallery3 = request.FILES.get("gallery3")
        img_obj.gallery4 = request.FILES.get("gallery4")
        img_obj.gallery5 = request.FILES.get("gallery5")
        img_obj.gallery6 = request.FILES.get("gallery6")

# Save to database
        img_obj.save()

        guest_text = request.POST.get("guest_list")

        if guest_text:
            names = guest_text.split("\n")

            for name in names:
                name = name.strip()
                if name:
                    Guest.objects.create(
                        guest_name=name,
                        wedding=wedding
                    )

        return redirect('home')


    return render(request, 'couplesInfo.html')

def rsvp_page(request, wedding_id):
    wedding = Wedding.objects.get(id=wedding_id)
    guests = Guest.objects.filter(wedding=wedding)

    if request.method == "POST":
        guest_id = request.POST.get("guest_id")
        number = request.POST.get("number_of_guests")
        attendance = request.POST.get("attendance")

        guest = Guest.objects.get(id=guest_id)

        # Example: Save RSVP
        RSVP.objects.create(
            guest=guest,
            number_of_guests=number,
            attendance=attendance
        )

    return render(request, "rsvp.html", {
        "wedding": wedding,
        "guests": guests
    })
