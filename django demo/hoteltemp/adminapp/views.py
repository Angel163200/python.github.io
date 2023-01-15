from django.shortcuts import render

# Create your views here.
import user
from adminapp.models import Rooms
from user.models import Registration, Login, Book, Feedback


def admin(request):
    return render(request, "admin/admin.html")


def admins(request):
    return render(request, "admin/admins.html")


def view_users(request):
    users = Registration.objects.filter(loginid__role=1)
    return render(request, "admin/view_users.html", {'users': users, 'table': 'User Details'})


def view_feedbacks(request):
    feed = Feedback.objects.raw('SELECT * from user_feedback')
    return render(request, "admin/view_feedbacks.html", {'feed': feed, 'table': 'Feedbacks'})


def delete_user(request, id):
    u = Registration.objects.get(id=id)
    log = u.loginid_id
    l = Login.objects.get(id=log)
    u.delete()
    l.delete()
    users = Registration.objects.raw('SELECT * from user_registration')
    return render(request, "admin/view_users.html", {'users': users})


def view_rooms(request):
    rooms = Rooms.objects.raw('SELECT * from adminapp_rooms')
    return render(request, "admin/view_rooms.html", {'rooms': rooms, 'table': 'Room Details'})


def edit_rooms(request, id):
    if request.method == 'POST':
        rooms = Rooms.objects.get(id=id)
        if len(request.FILES) != 0:
            rooms.r_image = request.FILES['image']
        rooms.room_no = request.POST.get('roomno')
        rooms.floor_no = request.POST.get('floorno')
        rooms.type = request.POST.get('type')
        rooms.size = request.POST.get('size')
        rooms.capacity = request.POST.get('capacity')
        rooms.view = request.POST.get('view')
        rooms.location = request.POST.get('location')
        rooms.price = request.POST.get('price')
        rooms.save()
        room = Rooms.objects.all()
        return render(request, "admin/view_rooms.html", {'rooms': room})
    rooms = Rooms.objects.get(id=id)
    return render(request, "admin/edit_rooms.html", {'rooms': rooms})


def add_rooms(request):
    if request.method == 'POST':
        if len(request.FILES) != 0:
            image = request.FILES['image']
        else:
            image = 'images/default.jpg'
        roomno = request.POST.get("roomno")
        floorno = request.POST.get("floorno")
        type = request.POST.get("type")
        size = request.POST.get("size")
        capacity = request.POST.get("capacity")
        view = request.POST.get("view")
        location = request.POST.get("location")
        price = request.POST.get("price")

        roomobj = Rooms()
        roomobj.r_image = image
        roomobj.floor_no = floorno
        roomobj.room_no = roomno
        roomobj.floor_no = floorno
        roomobj.type = type
        roomobj.size = size
        roomobj.capacity = capacity
        roomobj.view = view
        roomobj.location = location
        roomobj.price = price
        roomobj.save()

        return render(request, "admin/admin.html")
    return render(request, "admin/add_rooms.html")


def delete_rooms(request, id):
    room = Rooms.objects.get(id=id)
    room.delete()
    room = Rooms.objects.raw('SELECT * from adminapp_rooms')
    return render(request, "admin/view_rooms.html", {'rooms': room})


def view_booked_rooms(request):
    book = Book.objects.raw('SELECT * from user_book where status=1 order by check_in asc')
    return render(request, "admin/view_booked_rooms.html", {'book': book, 'table': 'Booking Details'})


def kochi_rooms(request):
    rooms = Rooms.objects.raw('SELECT * from adminapp_rooms')
    return render(request, "admin/kochi.html", {'rooms': rooms, 'table': 'Room Details'})


