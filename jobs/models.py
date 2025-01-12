from django.db import models
from django.urls import reverse

class PublicationManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(published=Publication.Status.PUBLISHED)

class Publication(models.Model):
    class Status(models.IntegerChoices):
        ARCHIVE=0, "Archive"
        PUBLISHED=1, "Published"
    title=models.CharField(max_length=255)
    slug=models.SlugField(max_length=255, unique=True, db_index=True, null=True)
    content=models.TextField()
    time_create=models.DateTimeField(auto_now_add=True)
    time_update=models.DateTimeField(auto_now=True)
    published=models.BooleanField(choices=Status.choices, default=Status.PUBLISHED)
    company = models.ForeignKey("Company", on_delete=models.CASCADE)

    objects=models.Manager()
    is_published=PublicationManager()

    def __str__(self):
        return self.title

    def get_url(self):
        return reverse("publication", kwargs={"publication_slug":self.slug})

    class Meta:
        ordering=["-time_create"]
        indexes=[
            models.Index(fields=["-time_create"])
        ]


class Company(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name



