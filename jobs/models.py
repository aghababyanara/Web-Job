from django.db import models

class Publication(models.Model):
    title=models.CharField(max_length=255)
    content=models.TextField()
    time_create=models.DateTimeField(auto_now_add=True)
    time_update=models.DateTimeField(auto_now=True)
    published=models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering=["-time_create"]
        indexes=[
            models.Index(fields=["-time_create"])
        ]




