from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("websites/", views.websites_view, name="websites_view"),
    path("website/<int:website_id>/", views.detail, name="detail"),
    path("website/<int:website_id>/maintenance", views.maintenance, name="maintenance"),
    path("website/test", views.test, name="test"),
]