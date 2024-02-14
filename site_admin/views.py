from django.shortcuts import render,redirect
from site_admin.models import *
from buyer.models import *
from seller.models import *
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"index.html")


def admin_login(request):
    return render(request,"login.html")


def login_action(request):
    Username=request.POST['username']
    Password=request.POST['password']
    username=request.POST['username']
    password=request.POST['password']
    admin=Admin_tb.objects.filter(Username=Username,Password=Password)
    user=register_table.objects.filter(Username=Username,Password=Password)
    seller=seller_table.objects.filter(username=username,password=password)
    if(admin.count()>0):
        request.session["adminid"]=admin[0].id
        return render(request,"adminhome.html")
    elif(user.count()>0):
        request.session["userid"]=user[0].id
        return render(request,"userhome.html")
    elif(seller.count()>0):
        if(seller[0].status == "approved"):
            request.session["sellerid"]=seller[0].id
            return render(request,"seller_home.html")
        else:
            messages.add_message(request,messages.INFO,"seller not approved")
        return redirect(index)
    
def addcategory(request):
    return render(request,"addcategory.html")  

def categoryaction(request):
    categoryname=request.POST['categoryname'] 
    user=Category_tb(categoryname=categoryname)
    user.save()
    messages.add_message(request,messages.INFO,"category added successfully")
    return redirect(addcategory) 

def viewseller(request):
    user=seller_table.objects.all()
    return render(request,"viewseller.html",{'view':user})

def statusapprove(request,id):
    seller_table.objects.filter(id=id).update(status="approved")
    return redirect('viewseller')

def statusreject(request,id):
    seller_table.objects.filter(id=id).update(status="reject")
    return redirect('viewseller')

def username(request):
    return render(request,"forgotpassword.html")

def forgotpassword(request):
     username=request.POST['usname']
     
     user=register_table.objects.filter(Username=username)
     seller=seller_table.objects.filter(username=username)

     if(user.count()>0):
         return render(request,"forgotpassword1.html",{'view':username})
     
     elif(seller.count()>0):
         return render(request,"forgotpassword1.html",{'view':username})    
     else:
        messages.add_message(request,messages.INFO,"enter a valid username")
        return redirect(forgotpassword)
     
def forgotpassword1(request):
    username=request.POST['usname']
    name=request.POST['name']
    dob=request.POST['dob']
    phone=request.POST['phone']
    
    user=register_table.objects.filter(Name=name,Mobile=phone,DOB=dob)
    seller=seller_table.objects.filter(name=name,mobile=phone,dob=dob)

    if(user.count()>0):
         return render(request,"forgotpassword2.html",{'view':username})
     
    elif(seller.count()>0):
         return render(request,"forgotpassword2.html",{'view':username})    
    else:
        messages.add_message(request,messages.INFO,"enter a valid details")
        return redirect(forgotpassword1)

def forgotpassword2(request):
    username=request.POST['usname']
    newpassword=request.POST['newpassword']
    conformpassword=request.POST['conformnewpassword']

    if(newpassword == conformpassword):
         buyer=register_table.objects.filter(Username=username)
         seller=seller_table.objects.filter(username=username)
         if(buyer.count()>0):
             buyerid=buyer[0].id
             register_table.objects.filter(id=buyerid).update(Password=conformpassword)
             messages.add_message(request,messages.INFO,"password changed")
             return render(request,"login.html")
        
         
         elif(seller.count()>0):
                 sellerid=seller[0].id
                 seller_table.objects.filter(id=sellerid).update(password=conformpassword)
                 messages.add_message(request,messages.INFO,"password changed")
                 return render(request,"login.html")
        

    else:   
          messages.add_message(request,messages.INFO,"invalid username or password")
          return render(request,"login.html")

def logout(request):
    request.session.flush()
    return render(request,"index.html")

            