from django.urls import path
from . import views

urlpatterns = [
    path("", views.alerts_page, name="alerts_page"),
]
