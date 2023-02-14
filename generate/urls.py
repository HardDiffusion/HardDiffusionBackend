"""generate URL Configuration"""
from django.urls import path

from generate import views

urlpatterns = [
    path("", views.index, name="generate_index"),
    path("images", views.images, name="images"),
    path("queue_prompt", views.queue_prompt, name="queue_prompt"),
    path("renderer_health", views.renderer_health, name="renderer_health"),
]
