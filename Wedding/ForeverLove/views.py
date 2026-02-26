from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # save new user
            login(request, user)  # log the user in immediately
            return redirect('Info')  # redirect to couples info or home
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})

def home_page(request):
    weddings=Wedding.objects.last()
    img_obj=Image.objects.filter(wedding=weddings).last()
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
    weddings = Wedding.objects.last() 
    img = Image.objects.filter(wedding=weddings).first()
    return render(request, 'story.html', {'weddings':weddings, 'img':img})

def galler_page(request):
    weddings = Wedding.objects.last() 
    img = Image.objects.filter(wedding=weddings).first()    
    return render(request, 'gallery.html', {'weddings':weddings, 'img':img})

@login_required
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
        date_of_meet=request.POST.get("dateOfMeet")
        first_date = request.POST.get("first_date")
        date_of_fdate=request.POST.get("dateOfDate")
        proposal = request.POST.get("proposal")
        date_of_proposal=request.POST.get("dateOfProposal")
        engagement = request.POST.get("engagement")
        date_of_engagement=request.POST.get("dateOfEngagement")
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
            marriage=marriage,
            dateOfMeet=date_of_meet,
            dateOfDate=date_of_fdate,
            dateOfProposal=date_of_proposal,
            dateOfEngagement=date_of_engagement
        )
             # Create Image object linked to this wedding
        img_obj = Image(wedding=wedding)

# Assign each uploaded file individually
   
        img_obj.herImage = request.FILES.get("herImage")
        img_obj.hisImage = request.FILES.get("hisImage")
        img_obj.meet = request.FILES.get("meet")
        img_obj.engagement = request.FILES.get("engaement")
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
        attending_bool = True if attendance == 'yes' else False

        try:
            number = int(number)
        except (TypeError, ValueError):
            number = 1  # default if empty or invalid

        # Example: Save RSVP
        RSVP.objects.create(
            wedding=wedding, 
            guest=guest,
            numberofGuste=number,
            attending=attending_bool
        )

        return redirect('home')

    return render(request, "rsvp.html", {
        "wedding": wedding,
        "guests": guests
    })

def edit_wedding(request):
    wedding = Wedding.objects.last()

    if not wedding:
        return redirect('Info')

    if request.method == "POST":
        wedding.bride_name = request.POST.get('bride_name')
        wedding.groom_name = request.POST.get('groom_name')
        wedding.wedding_date = request.POST.get('wedding_date')
        wedding.location = request.POST.get('location')
        wedding.story = request.POST.get('story')
        wedding.herStory = request.POST.get('herStory')
        wedding.hisStory = request.POST.get('hisStory')
        wedding.how_we_met = request.POST.get('how_we_met')
        wedding.first_date = request.POST.get('first_date')
        wedding.proposal = request.POST.get('proposal')
        wedding.engagement = request.POST.get('engagement')
        wedding.marriage = request.POST.get('marriage')
        wedding.dateOfMeet=request.POST.get('dateOfMeet')
        wedding.dateOfDate=request.POST.get('dateOfDate')
        wedding.dateOfProposal=request.POST.get('dateOfProposal')
        wedding.dateOfEngagement=request.POST.get('dateOfEngagement')

        wedding.save()
        return redirect('Info')

    context = {
        'wedding': wedding
    }

    return redirect('home')


    return render(request, 'update.html', context)
