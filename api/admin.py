from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.NewsText)
admin.site.register(models.AboutUsText)
admin.site.register(models.ContactUsText)
admin.site.register(models.SliderPhoto)
admin.site.register(models.RatingsText)
admin.site.register(models.SubEmail)