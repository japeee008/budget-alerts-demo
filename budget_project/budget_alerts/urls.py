from django.urls import path
from . import views

urlpatterns = [
    path('health/', views.health, name='budget_alerts_health'),
    path("", views.alerts_page, name="alerts_page"),
]
