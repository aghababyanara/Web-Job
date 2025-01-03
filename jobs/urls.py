from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("categories/", views.companies, name="companies"),
    path("add-publication/", views.add_publication, name="add_publication"),
    path("contacts/", views.contacts, name="contacts"),
    path("login/", views.login, name="login"),
    path("posts/<int:post_id>", views.post_more, name="posts")
]
