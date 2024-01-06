from . import views
from django.urls import path

app_name="Rent"

urlpatterns = [
    path('',views.home,name="home"),
]