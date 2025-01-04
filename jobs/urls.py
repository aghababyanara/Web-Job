from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("companies/", views.companies, name="companies"),
    path("add-publication/", views.add_publication, name="add_publication"),
    path("contacts/", views.contacts, name="contacts"),
    path("login/", views.login, name="login"),
    path("publication/<slug:publication_slug>/", views.show_publication, name="publication")
]
