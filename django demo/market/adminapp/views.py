from django.shortcuts import render
from login.models import User, Login, Feedback


def admin(request):
    return render(request, 'admin/admin.html')

def delete_user(request,id):
    u=User.objects.get(id=id)
    log = u.loginid_id
    role=u.role
    l = Login.objects.get(id=log)
    u.delete()
    l.delete()
    if role == 1:
        users = User.objects.raw('SELECT * from login_user where role=1 and status="accept" ')
        return render(request, "admin/user_table.html", {'users': users})
    if role == 2:
        users = User.objects.raw('SELECT * from login_user where role=2')
        return render(request, "admin/user_table.html", {'users': users})

def accept_seller(request,id):
    l=User.objects.get(id=id)
    l.status="accept"
    l.save()
    users =User.objects.raw('SELECT * from login_user where status="not" order by date desc')
    return render(request, "admin/accept_seller_table.html", {'users': users})

def accept_seller1(request):
    users =User.objects.raw('SELECT * from login_user where status="not" order by date desc')
    return render(request, "admin/accept_seller_table.html", {'users': users})

def view_seller(request):
    users = User.objects.raw('SELECT * from login_user where role=1 and status="accept"')
    return render(request, "admin/user_table.html", {'users': users,'table':'Seller Details'})

def view_customer(request):
    users = User.objects.raw('SELECT * from login_user where role=2')
    return render(request, "admin/user_table.html", {'users': users,'table':'Customer Details'})


def view_customer_feedback(request):
    users = Feedback.objects.raw('SELECT * from login_feedback where role=2 order by date desc')
    return render(request, "admin/user_feedback.html", {'users': users,'feed':'Customer Feedback'})

def view_seller_feedback(request):
    users = Feedback.objects.raw('SELECT * from login_feedback  where role=1 order by date desc')
    return render(request, "admin/user_feedback.html", {'users': users,'feed':'Seller Feedback'})
