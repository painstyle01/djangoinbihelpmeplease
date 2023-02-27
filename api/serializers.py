import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import AboutUsText, ContactUsText, NewsText, SliderPhoto, RatingsText, SubEmail
from rest_framework import serializers
from django.views.decorators.csrf import csrf_exempt


class NewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NewsText
        fields = ('text',)


class AboutUsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AboutUsText
        fields = ('text',)


class ContactUsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContactUsText
        fields = ('text',)


class SliderPhotoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SliderPhoto
        fields = ('file',)


class RatingsTextSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RatingsText
        fields = ('name', 'text', 'file')


class EmailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SubEmail
        fields = ("email",)
