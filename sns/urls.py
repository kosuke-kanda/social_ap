from django.urls import path

from . import views

app_name = "sns"

urlpatterns = [
    # path("top/", views.top_view, name="top"),
    path('top/', views.TopView.as_view(), name="top"),
    path("", views.TimeLineView.as_view(), name="list"),
    path("create/", views.CreatePostView.as_view(), name="create"),
]