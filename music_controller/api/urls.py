from django.urls import path
from . import views

urlpatterns = [
    path("room", views.RoomView.as_view(), name = "room"),
    path("admin", views.RoomAdmin.as_view(), name = "admin"),    
    path('create-room', views.CreateRoomView.as_view(), name="create"),    
    path('get-room', views.GetRoom.as_view(), name="get")
]