from django.urls import path

from . import views

urlpatterns = [
    path('menu/', views.IndexView.as_view(), name='menu'),
]
