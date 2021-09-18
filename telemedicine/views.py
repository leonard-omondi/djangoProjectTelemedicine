from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Dummy data
posts = [
    {
        'name': 'John Doe',
        'age': '19',
        'sex': 'Male',
        'last_visit': 'January 1, 2021'
    },
    {
        'name': 'Jane Doe',
        'age': '20',
        'sex': 'Female',
        'last_visit': 'April 1, 2021'
    }
]


# Handles traffic to our homepage
def home(request):
    context = {
        'posts': Post.objects.all()  # Queries data from our database
    }
    return render(request, 'telemedicine/home.html', context)


def about(request):
    context = {
        'posts': posts
    }
    return render(request, 'telemedicine/about.html', {'title': 'About'})


def contact(request):
    return render(request, 'telemedicine/contact.html')


def patient(request):
    return render(request, 'telemedicine/about.html')


def physician(request):
    return render(request, 'telemedicine/about.html')
