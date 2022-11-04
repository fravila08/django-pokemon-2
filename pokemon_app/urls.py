from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path("pokemon/<str:type>", views.teamType, name="byType"),
    path("items", views.showItems)
]