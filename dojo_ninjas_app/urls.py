from django.urls import path
from dojo_ninjas_app import views

urlpatterns = [
    path('', views.index)
]