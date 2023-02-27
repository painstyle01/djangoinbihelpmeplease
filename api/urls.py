from django.urls import include, re_path, path
from rest_framework import routers
from .views import ContactUsViewset, NewsViewset, AboutUsViewset, SliderPhotosViewset, RatingTextViewset, save_email

router = routers.DefaultRouter()

router.register(r'contact_us', ContactUsViewset)
router.register(r'news', NewsViewset)
router.register(r'aboutus', AboutUsViewset)
router.register(r"slider", SliderPhotosViewset)
router.register(r"rating", RatingTextViewset)
# Привязываем наше API используя автоматическую маршрутизацию.
# Также мы подключим возможность авторизоваться в браузерной версии API.

urlpatterns = [
    path(r"save_email", save_email, name="save_email"),
    re_path(r'^', include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]