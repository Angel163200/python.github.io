from django.shortcuts import render
from adminapp.models import Course
from loginapp.models import Login, User,Course


def login(request):
    if request.method=='POST':

        user = request.POST.get("uname")
        pwd = request.POST.get("passwd")

        if Login.objects.filter(username=user,password=pwd).exists():
            currentuser = Login.objects.get(username=user,password=pwd)

            request.session['userid']= currentuser.id

            if currentuser.role==0:
                users = User.objects.all()
                return render(request,"admin/adminhome.html",{'users':users})
            else:
                user = User.objects.get(loginid=currentuser)
                return render(request,"user/profile.html",{'user':user})
        else:
            return render(request, "common/login.html",{'error':'Login failed'})
    return render(request,"common/login.html")

def register(request):
    if request.method=='POST':
        name = request.POST.get("name")
        dob = request.POST.get("dob")
        email = request.POST.get("email")
        course=request.POST.get("ddlcourse") #2
        user = request.POST.get("uname")
        pwd = request.POST.get("passwd")

        if len(request.FILES)!=0:
            pp = request.FILES['pp']
        else:
            pp = 'images/default.jpeg'
        loginobj = Login()
        loginobj.username=user
        loginobj.password=pwd
        loginobj.save()

        userobj= User()
        userobj.loginid = loginobj
        userobj.name = name
        userobj.dob=dob
        userobj.email=email
        userobj.courseid=Course.objects.get(id=course)
        userobj.profilepic=pp
        userobj.save()
        return render(request,"common/login.html")
    c=Course.objects.all()
    return render(request,"common/registration.html",{'c':c})

def update(request):
    if "userid" in request.session:
        userid=request.session["userid"]
        user=User.objects.get(loginid_id=userid)
        user.name=request.POST.get('name')
        user.email = request.POST.get("email")
        if len(request.FILES)!=0:
            user.profilepic = request.FILES['pp']
        user.save()

        return render(request, "user/profile.html", {'user': user})
    return render(request, "common/login.html")


