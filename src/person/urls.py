from django.urls import path
from . import views

urlpatterns = [

    path('add/', views.add_person),
    path('show/', views.get_all_person)
]