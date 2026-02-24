from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, 'homePage.html')

def about_page(request):
    return render(request, 'aboutPage.html')

def story_page(request):
    return render(request, 'story.html')

def galler_page(request):
    return render(request, 'gallery.html')
