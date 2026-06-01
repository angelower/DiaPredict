from django.urls import path
from . import views

urlpatterns = [
    path('', views.predecir_diabetes, name='predecir_diabetes'),
]