from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class AboutUsText(models.Model):
    text = RichTextField()


class NewsText(models.Model):
    text = RichTextField()


class ContactUsText(models.Model):
    text = RichTextField()


class SliderPhoto(models.Model):
    file = models.ImageField(upload_to="media/")


class RatingsText(models.Model):
    name = models.TextField()
    text = RichTextField()
    file = models.FileField(upload_to="media/docs/")

    def __str__(self):
        return f"{self.name}"


class SubEmail(models.Model):
    email = models.TextField()

    def __str__(self):
        return f"{self.email}"
