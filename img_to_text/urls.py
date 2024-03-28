from django.urls import path
from img_to_text import views

urlpatterns = [
    path('', views.extract_text_from_image, name='img2txt'),
]
