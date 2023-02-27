import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import AboutUsText, ContactUsText, NewsText, SliderPhoto, RatingsText, SubEmail
from rest_framework import viewsets
from .serializers import AboutUsSerializer, ContactUsSerializer, NewsSerializer, SliderPhotoSerializer, \
    RatingsTextSerializer


# Create your views here.
class AboutUsViewset(viewsets.ModelViewSet):
    queryset = AboutUsText.objects.all()
    serializer_class = AboutUsSerializer


class NewsViewset(viewsets.ModelViewSet):
    queryset = NewsText.objects.all()
    serializer_class = NewsSerializer


class ContactUsViewset(viewsets.ModelViewSet):
    queryset = ContactUsText.objects.all()
    serializer_class = ContactUsSerializer


class SliderPhotosViewset(viewsets.ModelViewSet):
    queryset = SliderPhoto.objects.all()
    serializer_class = SliderPhotoSerializer


class RatingTextViewset(viewsets.ModelViewSet):
    queryset = RatingsText.objects.all()
    serializer_class = RatingsTextSerializer


@csrf_exempt
def save_email(request):
    if request.method == "POST":
        data = json.loads(request.body.decode())
        email = data["email"]
        email_instance = SubEmail.objects.create(email=email)
        email_instance.save()
        print(email_instance)
        return HttpResponse(email_instance)
    else:
        return HttpResponse(403)
