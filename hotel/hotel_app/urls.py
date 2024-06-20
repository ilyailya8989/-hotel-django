from django.urls import path

from hotel_app import views

urlpatterns = [
    path('rooms/', views.first_list, name='first'),
    path('rooms/<int:room_id>', views.info_list, name='second'),
    path('rooms/add_room/', views.add_room, name='add_room'),



]