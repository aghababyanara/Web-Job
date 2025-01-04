from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.db import models
from .models import Publication


def index(request):
    publications=Publication.is_published.all()
    return render(request, "jobs/index.html", {"publications":publications})


def companies(request):
    return render(request,"jobs/companies.html", {"title":"Companies"})

def show_publication(request, publication_slug):
    publication=get_object_or_404(Publication, slug=publication_slug)

    data={
        "title":publication.title,
        "content":publication.content,
        "time_create":publication.time_create,
        "time_update":publication.time_update,
        "published":publication.published
    }
    return render(request, "jobs/show-publication.html", data)

def add_publication(request):
    return render(request, "jobs/add-publication.html", {"title":"Add Publication"})


def contacts(request):
    return render(request, "jobs/contacts.html", {"title":"Contacts"})

def login(request):
    return render(request, "jobs/login.html", {"title":"Login"})
