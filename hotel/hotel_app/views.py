from django.shortcuts import render, get_object_or_404, redirect

from hotel_app.models import Hotel, Room


# Create your views here.
def first_list(request):
    rooms = Room.objects.all()
    return render(request,'hotel_app/hotel_list.html',{'rooms':rooms})

def info_list(request, room_id):
    rooms = get_object_or_404(Room, id=room_id)
    return render(request, 'hotel_app/info_room.html',{'rooms': rooms})

def add_room(request):
    hostel = get_object_or_404(Hotel, id=1)

    if request.method == 'POST':
        numbers = request.POST.get('numbers')
        classification = request.POST.get('classification')
        priceOnNight = request.POST.get('priceOnNight')
        description = request.POST.get('description')
        rooms = request.POST.get('rooms')

        if numbers and classification and priceOnNight and description and rooms:
            Room.objects.create(numbers=numbers,classification=classification,priceOnNight=priceOnNight,description=description, rooms=rooms)

            return redirect('first')

    return render(request, 'hotel_app/add_room.html', {'hostel':hostel})
