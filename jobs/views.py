from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string



data_from_db=[
    {
    "id":1,
    "is_published":True,
    'title': "Game Presenter-Morning Shift",
    "content":"""Job responsibilities
    • Be the face of our award-winning products;
    • Lead the game according to the instructions on the screen;
    • Communicate with our product users from around the world.
    • Ability to work only with morning shift-08:00 – 16:00"""
    },
    {
    "id":2,
    "title":"Insurance Assistant (Remote)Los Angeles, CA",
    "is_published":True,
    "content":"""Job Description
    We are seeking a detail-oriented and reliable Insurance Assistant to join our team remotely. 
    You will also help maintain client records, process billing inquiries, and ensure excellent customer service.
    The ideal candidate will have strong organizational and communication skills, attention to detail, and the ability to handle administrative tasks efficiently. 
    Experience in insurance is preferred but not required.
    Qualifications: High school diploma, strong communication skills, proficiency in Microsoft Office, and the ability to work independently. 
    Join us for a flexible and rewarding remote position with opportunities for professional growth.
    """
    }
]

def index(request):
    data={
        "title":"Home Page",
        "description":"its home page",
        "posts":data_from_db
    }
    return render(request, "jobs/index.html", context=data)


def companies(request):
    return render("base.html", {"title":"Companies"})

def post_more(request, post_id):
    return render(request, "jobs/read-more.html", {"title":"Read More"})

def add_publication(request):
    return render(request, "jobs/add-publication.html", {"title":"Add Publication"})

def contacts(request):
    return render(request, "jobs/contacts.html", {"title":"Contacts"})

def login(request):
    return render(request, "jobs/login.html", {"title":"Login"})
