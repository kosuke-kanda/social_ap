from django.urls import path

from . import views

app_name = "sns"

urlpatterns = [
    path("top/", views.top_view, name="top"),
]