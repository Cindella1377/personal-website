from django.shortcuts import render

name = [
    {"name": "Buy flowers", "completed": True},
    {"name": "Go to the Mars", "completed": True},
    {"name": "Take a break", "completed": False},
    {"name": "Get orgainzied", "completed": True},
    {"name": "Watch a movie", "completed": False},
]

def home(request):
    return render(request, "home.html", {"tasks": name})

def about(request):
    return render(request, "about.html")
    
def contact(request):
    return render(request, "contact.html")
