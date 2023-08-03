from django.urls import path
from . import views
urlpatterns = [
    path('', views.eventdetails.as_view()),
]