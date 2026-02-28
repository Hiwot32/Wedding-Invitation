from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  
            login(request, user)  
            return redirect('home') 
    else:
        form = UserCreationForm()
    return render(request, 'registration.html', {'form': form})



def user_login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {"error":"Invalid Credentials"})
        
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('home')

def home_page(request):
    weddings=Wedding.objects.last()
    img_obj=Image.objects.filter(wedding=weddings).last()

    if not weddings:
        weddings={
            "bride_name":"Sara",
            "groom_name":"Abrham",
            "location":"Mexico, Naer Debrework Building",
            "wedding_date":"May 12, 2026",
            
        }
 
    context={
        "weddings":weddings,
        "img_obj":img_obj
    }
    return render(request, 'homePage.html', context)


def about_page(request):
    weddings=Wedding.objects.last()
    img=Image.objects.filter(wedding=weddings).last()
    if not weddings:
        weddings={
            "bride_name":"Sara",
            "groom_name":"Abrham",
            "herStory":"She grew up surrounded by love, kindness, and strong family values. With a warm heart and a bright smile, she has always brought joy to those around her. She believes in faith, hard work, and the beauty of simple moments. Today, she begins a new chapter as a bride — ready to build a life filled with love, laughter, and lasting memories.",
            "hisStory":"He was raised with strong values, a caring heart, and a determined spirit. Known for his kindness and quiet strength, he has always worked hard to build a meaningful life. He finds joy in family, friendship, and the simple blessings each day brings.Today, he steps into a new chapter as a groom — ready to lead with love, stand with loyalty, and build a future filled with happiness and lasting memories."          
        }
    
    context={
        "weddings":weddings,
        "img":img
    }
    return render(request, 'aboutPage.html', context)


def story_page(request):
    weddings=Wedding.objects.last()
    img=Image.objects.filter(wedding=weddings).last()

    if not weddings:
        weddings={
            "bride_name":"Sara",
            "groom_name":"Abrham",
            "how_we_met":"Their story began with a simple introduction that turned into hours of easy conversation. What started as friendship slowly grew into something deeper, built on laughter, understanding, and shared dreams.From that first meeting, their hearts knew they had found something special — a love meant to last a lifetime.",
            "dateOfMeet":"April 1, 2024",
            "first_date":"Their first date was simple but unforgettable. Nervous smiles quickly turned into comfortable laughter as they talked for hours, losing track of time. In that quiet moment, they both felt something special — the beginning of a beautiful love story.",
            "dateOfDate":"Augest 2, 2024",
            "proposal":"On a beautiful and unforgettable day, he planned a moment filled with love and meaning. With a nervous smile and a hopeful heart, he asked her to spend forever with him.Through happy tears and a joyful “yes,” their journey toward a lifetime together officially began.",
            "dateOfProposal":"Jun 24, 2025",
            "engagement":"Their engagement was a joyful celebration of love, family, and new beginnings. Surrounded by the people who mean the most to them, they promised to walk hand in hand through every season of life.It was the start of a beautiful chapter — filled with excitement, hope, and dreams of forever.",
            "dateOfEngagement":"April 2, 2026",
            "marriage":"On their special day, surrounded by love and blessings, they promised to stand by each other through every joy and challenge. With grateful hearts and hopeful dreams, they began their life as one.Their marriage marks the beginning of a forever built on love, trust, and unwavering commitment."
        }

    context={
        "weddings":weddings,
        "img":img
    }
    return render(request, 'story.html', context)



def gallery_page(request):
    weddings=Wedding.objects.last()
    img=Image.objects.filter(wedding=weddings).last()
    if not weddings:
        weddings={
            "bride_name":"Sara",
            "groom_name":"Abrham",
        } 
    context={
        "weddings":weddings,
        "img":img
    }
    return render(request, 'gallery.html', context)



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
        
        Image.objects.create(
            wedding=wedding,
            herImage=request.FILES.get("herImage"),
            hisImage=request.FILES.get("hisImage"),
            meetImg=request.FILES.get("meet"),
            engagementImg=request.FILES.get("engagement"),
            first_dateImg=request.FILES.get("first_date"),
            proposalImg=request.FILES.get("proposal"),
            marriageImg=request.FILES.get("marriage"),
            gallery1=request.FILES.get("gallery1"),
            gallery2=request.FILES.get("gallery2"),
            gallery3=request.FILES.get("gallery3"),
            gallery4=request.FILES.get("gallery4"),
            gallery5=request.FILES.get("gallery5"),
            gallery6=request.FILES.get("gallery6"),
        )
    

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
    wedding=Wedding.objects.get(id=wedding_id)
    guests=Guest.objects.filter(wedding=wedding)

    if request.method=="POST":
        guest_id=request.POST.get('guest_id')
        number=request.POST.get('number')
        attendance=request.POST.get('attending')
        comments=request.POST.get('comments')

        guest=Guest.objects.get(id=guest_id)
        attending=True if attendance == "yes" else False


        number=int(number) if number else 1

        RSVP.objects.create(
            wedding=wedding,
            guest=guest,
            attending=attending,
            number_of_guests=number,
            comment=comments
        )
    return render(request, 'RSVP.html', {'wedding':wedding, 'guests':guests})



def edit_wedding(request):
    wedding = Wedding.objects.last()

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

    # return redirect('home')

    return render(request, 'update.html', context)


def rsvp_summary(request):
    wedding = Wedding.objects.last()
    rsvps = RSVP.objects.filter(wedding=wedding)
    
    context = {
        'wedding': wedding,
        'rsvps': rsvps
    }
    
    return render(request, 'rsvp_summary.html', context)

def delete_info(request):
    wedding=Wedding.objects.last()
    wedding.delete()
    return render(request, 'deletePage.html')
