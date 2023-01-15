from pyexpat.errors import messages

import respond as respond
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from adminapp.models import Rooms
from user.models import Login, Registration, Book, Feedback
from datetime import datetime, date


def about(request):
    return render(request, 'about.html')


def index(request):
    feed = Feedback.objects.all()
    return render(request, "index.html", {'feed': feed})


def blog(request):
    return render(request, 'blog.html')


def blogdetails(request):
    return render(request, 'blog-details.html')


def roomdetails(request):
    return render(request, 'room-details.html')


def rooms(request):
    return render(request, 'book_rooms.html')


def select(request):
    if request.method == 'POST':
        dest = request.POST.get('destination')
        rooms = Rooms.objects.filter(location=dest)
        n = [1, 2, 3, 4, 5]
        return render(request, 'book_rooms.html', {'rooms': rooms, 'n': n})


#def destination(request, n):
    #rooms = Rooms.objects.filter(location=dest)
    #n = [1, 2, 3, 4, 5]
    #return render(request, 'book_rooms.html', {'rooms': rooms, 'n': n})

def login(request):
    if request.method == 'POST':

        user = request.POST.get("username")
        pwd = request.POST.get("password")

        if Login.objects.filter(username=user, password=pwd).exists():
            currentuser = Login.objects.get(username=user, password=pwd)

            request.session['userid'] = currentuser.id
            # request.session['userid'] = id

            if currentuser.role == 0:
                users = Registration.objects.all()
                return render(request, "admin/admin.html", {'users': users})
            else:
                user = Registration.objects.get(loginid=currentuser)
                request.session['username'] = user.loginid.username
                feed = Feedback.objects.all()
                return render(request, "index.html", {'feed': feed})
        else:
            return render(request, "login.html", {'error': 'Login failed'})
    return render(request, "login.html")


def registration(request):
    if request.method == 'POST':
        user = request.POST.get("username")
        phn = request.POST.get("phone")
        email = request.POST.get("email")
        pwd = request.POST.get("password")
        confirm = request.POST.get("confirm")

        loginobj = Login()
        loginobj.username = user
        loginobj.password = pwd
        loginobj.save()

        userobj = Registration()
        userobj.loginid = loginobj
        userobj.phone = phn
        userobj.email = email
        userobj.confirm = confirm

        userobj.save()
        return render(request, "login.html")
    return render(request, "registration.html")


def check(request):
    if "userid" in request.session:
        return render(request, "registration.html")
    return render(request, "login.html")


def check_username(request):
    username=request.GET["id"]
    count = Login.objects.filter(username=username).count()
    if count==0:
        return HttpResponse("User name Available")
    else:
        return HttpResponse("Username Already Exist")


def change_psw(request):
    if request.method == 'POST':
        psw1 = request.POST.get("psw1")
        userid = request.session["userid"]
        if Login.objects.filter(id=userid, password=psw1).exists():
            l = Login.objects.get(id=userid)
            l.password = request.POST.get('pwd')
            l.save()
            return render(request, "login.html")
        else:
            return render(request, "common/change_psw.html", {'error': 'wrong password'})
    return render(request, 'common/change_psw.html')


def update_profile(request):
    if request.method == 'POST':
        if "userid" in request.session:
            userid = request.session["userid"]
            user = Registration.objects.get(loginid_id=userid)
            user1 = Login.objects.get(id=userid)
            user1.username = request.POST.get('username')
            user.phone = request.POST.get('phone')
            user.email = request.POST.get("email")
            user1.save()
            user.save()
            feed = Feedback.objects.all()
            return render(request, "index.html", {'feed': feed})

    user = Registration.objects.get(loginid_id=request.session['userid'])
    return render(request, 'common/update_profile.html', {'user': user})


def feedback(request):
    if request.method == 'POST':
        if "userid" in request.session:
            feedback = request.POST.get("feedback")
            userid = request.session["userid"]
            user = Login.objects.get(id=userid)

            feed = Feedback()
            feed.feedback = feedback
            feed.userid = user
            feed.username = user.username
            feed.date = date.today()
            feed.save()
            feed = Feedback.objects.all()
            return render(request, "index.html", {'feed': feed})

    return render(request, 'feedback.html')





def delete_account(request):
    if request.method == 'POST':
        uname = request.POST.get("uname")
        psw = request.POST.get("psw")

        if Login.objects.filter(username=uname, password=psw).exists():
            l = Login.objects.get(username=uname, password=psw)
            u = Registration.objects.get(loginid=l)
            u.delete()
            l.delete()
            return render(request, "login.html")
        else:
            return render(request, "common/delete_account.html", {'error': 'your Username or password is incorrect'})

    return render(request, 'common/delete_account.html')


def book_rooms(request):
    if request.method == 'POST':
        if "userid" in request.session:
            checkin = request.POST.get("checkin")
            checkout = request.POST.get("checkout")
            person = request.POST.get("persons")
            roomid = request.POST.get("ids")
            roomsobj = Rooms.objects.get(id=roomid)
            loginobj = Login.objects.get(id=request.session['userid'])

            bookobj = Book()
            bookobj.loginid = loginobj
            bookobj.roomid = roomsobj
            bookobj.check_in = checkin
            bookobj.check_out = checkout
            bookobj.persons = person
            bookobj.status = 0
            bookobj.save()
            check_in = datetime.strptime(checkin, "%Y-%m-%d")
            check_out = datetime.strptime(checkout, "%Y-%m-%d")
            date1 = date(check_in.year, check_in.month, check_in.day)
            date2 = date(check_out.year, check_out.month, check_out.day)
            date3 = date2 - date1
            n = date3.days
            total = bookobj.roomid.price * n + 300

            return render(request, "payment.html", {'book': bookobj, 'n': n, 'total': total})
        return render(request, "Login.html", {'error': 'You need to login to book your rooms'})
    return redirect('#')


def payment(request):
    if request.method == 'POST':
        bookid = request.POST.get("bid")
        bookobj = Book.objects.get(id=bookid)
        bookobj.status = 1
        bookobj.save()
        return render(request, 'payment.html', {'book': bookobj, 'n': 0, 'total': 0, 's': 1})


def logout(request):
    del request.session['userid']
    return render(request, "login.html")

# request.session['rid'] = id
# a = Rooms.objects.get(id=id)
# roomsobj = Rooms()
# bookobj.roomid = roomsobj()

# userid = request.session["userid"]
# u = Registration.objects.get(loginid_id=userid)
# bookobj.userid = u
# bookobj.username = u.username
