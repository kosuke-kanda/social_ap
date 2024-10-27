from django.urls import path

from . import views

app_name = "sns"

urlpatterns = [
    path('top/', views.TopView.as_view(), name="top"),
    path("", views.TimeLineView.as_view(), name="list"),
    path("user/<str:user>", views.UserPageView.as_view(), name="userPage"),
    path("create/", views.CreatePostView.as_view(), name="create"),
    path("delete/<int:pk>", views.DeltePost.as_view(), name="delete"),
]