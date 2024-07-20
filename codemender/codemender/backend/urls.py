from django.urls import path
from . import views

urlpatterns = [
    path('analyze/', views.analyze_code, name='analyze_code'),
    path('', views.health_check, name='health_check'),
]