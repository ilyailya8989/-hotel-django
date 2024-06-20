from django.urls import path

from hotel_app import views

urlpatterns = [
    path('', views.first_list, name='first'),
    path('rooms/<int:room_id>', views.info_list, name='second'),
    path('rooms/add_room/', views.add_room, name='add_room'),
    path('rooms/del_room/<int:room_id>', views.del_room, name='del_room'),
    path('rooms/edit_room/<int:room_id>', views.edit_room, name='edit_room'),



]