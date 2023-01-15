from datetime import date

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from login.models import Login, User, Feedback


def login(request):
    if request.method=='POST':

        uname = request.POST.get("uname")
        psw = request.POST.get("psw")

        if Login.objects.filter(username=uname,password=psw).exists():
            currentuser = Login.objects.get(username=uname,password=psw)
            currentuser.date = date.today()
            currentuser.save()

            if currentuser.role == 0:
                return render(request, "admin/admin.html")

            s = User.objects.get(loginid=currentuser)
            if s.status=="not":
                return render(request, "common/login.html", {'error': 'You are not accepted by the Admin'})
            request.session['userid'] = currentuser.id

            if currentuser.role == 1:
                user = User.objects.get(loginid=currentuser)
                return render(request, "seller/seller.html", {'user': user})
            if currentuser.role == 2:
                user = User.objects.get(loginid=currentuser)
                return render(request, "customer/customer.html", {'user': user})
        else:
            return render(request, "common/login.html", {'error': 'Login failed try again'})

    return render(request, 'common/login.html')

def register(request):
    if request.method=='POST':
        name = request.POST.get("name")
        address = request.POST.get("address")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        uname = request.POST.get("uname")
        psw = request.POST.get("psw")
        role= request.POST.get("role")

        if len(request.FILES)!=0:
            pp = request.FILES['pp']
        else:
            pp = 'images/default.jpeg'
        loginobj = Login()
        loginobj.username=uname
        loginobj.password=psw
        loginobj.role = role
        loginobj.save()

        userobj= User()
        userobj.loginid = loginobj
        userobj.name = name
        userobj.address = address
        userobj.email=email
        userobj.phone = phone
        userobj.profilepic=pp
        userobj.role = role
        userobj.date=date.today()
        if role== "2":
            userobj.status = "accept"
        else:
            userobj.status = "not"
        userobj.save()
        return render(request,"common/login.html")

    return render(request, 'common/register.html')

def update_profile(request):
    if request.method == 'POST':
        if "userid" in request.session:
            userid = request.session["userid"]
            user = User.objects.get(loginid_id=userid)
            user.name = request.POST.get('name')
            user.address = request.POST.get('address')
            user.phone = request.POST.get('phone')
            user.email = request.POST.get("email")
            if len(request.FILES) != 0:
                user.profilepic = request.FILES['pp']
            user.save()

            if user.role == 1:
                return render(request, "seller/seller.html")
            if user.role == 2:
                return render(request, "customer/customer.html")

    user = User.objects.get(loginid_id=request.session['userid'])
    return render(request, 'common/update_profile.html',{'user':user})

def feedback(request):
    if request.method == 'POST':
        if "userid" in request.session:
            feedback=request.POST.get("feedback")
            userid = request.session["userid"]
            u = User.objects.get(loginid_id=userid)
            role=u.role

            fed=Feedback()
            fed.feedback=feedback
            fed.role=role
            fed.userid=u
            fed.name=u.name
            fed.date=date.today()
            fed.save()
            if role == 1:
                return render(request, "seller/seller.html")
            if role == 2:
                return render(request, "customer/customer.html")

    return render(request, 'common/feedback.html')

def delete_account(request):
    if request.method=='POST':
        uname = request.POST.get("uname")
        psw = request.POST.get("psw")

        if Login.objects.filter(username=uname,password=psw).exists():
            l = Login.objects.get(username=uname,password=psw)
            u = User.objects.get(loginid=l)
            u.delete()
            l.delete()
            return render(request,"common/login.html")
        else:
            return render(request, "common/delete_account.html",{'error':'your Username or password is incorrect'})

    return render(request,'common/delete_account.html')

def change_psw(request):
    if request.method == 'POST':
        psw1 = request.POST.get("psw1")
        userid = request.session["userid"]
        if Login.objects.filter(id=userid,password=psw1).exists():
            l = Login.objects.get(id=userid)
            l.password= request.POST.get('psw')
            l.save()
            return render(request, "common/login.html")
        else:
            return render(request, "common/change_psw.html", {'error': 'wrong password'})
    return render(request, 'common/change_psw.html')

#ajax-jason
def checkusername(request):
    username=request.GET["id"]
    count = Login.objects.filter(username=username).count()
    if count==0:
        return HttpResponse("User name Available")
    else:
        return HttpResponse("Username Already Exist")

def checkph(request):
    phone=request.GET["id"]
    count = User.objects.filter(phone=phone).count()
    if count!=0:
        return HttpResponse("Phone Number Already Exist Try another one")
