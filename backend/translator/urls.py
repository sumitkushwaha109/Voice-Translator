from django.urls import path
from .views import translate_voice

urlpatterns = [
    path('translate/', translate_voice),
]