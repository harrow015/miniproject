from django.shortcuts import render, redirect
import datetime
from seller.models import *
from site_admin.models import Category_tb
from buyer.models import *
from django.contrib import messages

def sellerregistration(request):
    return render (request, "seller_registration.html")

def sellerregisteraction(request):
    name = request.POST["name"]
    address = request.POST['address']
    gender = request.POST['gender']
    place = request.POST['place']
    username = request.POST['username']
    password = request.POST['password']
    mobile = request.POST['mobile']
    dob = request.POST['dob']
    if len(request.FILES)>0:
        im = request.FILES['image']
    else:
        im="no pic"

    user = seller_table(
        name=name,
        address=address,
        gender=gender,
        place=place,
        username=username,
        password=password,
        dob=dob,
        mobile=mobile,
        image=im
    )
    user.save()
    messages.add_message(request,messages.INFO,"seller registeration successfull")
    return redirect("sellerregistration")

def sellereditinfo(request):
    seller=seller_table.objects.filter(id=request.session["sellerid"])
    return render(request,"sellereditinfo.html",{'view':seller})

def sellereditinfoaction(request):
    id=request.POST["id"]
    seller=seller_table.objects.filter(id=id)
    name = request.POST["name"]
    address = request.POST['address']
    gender = request.POST['gender']
    place = request.POST['place']
    username = request.POST['username']
    mobile = request.POST['mobile']
    dob = request.POST['dob']
    if len(request.FILES)>0:
        im = request.FILES['image']
    else:
        
        im=seller[0].image
        img=seller_table.objects.get(id=id)
        img.image=im
        img.save()
    user=seller_table.objects.filter(id=id).update(
        name=name,
        address=address,
        gender=gender,
        place=place,
        username=username,
        dob=dob,
        mobile=mobile,
        image=im

    )
    messages.add_message(request,messages.INFO,"seller information updatated")
    return redirect("sellereditinfo")

def product(request):
    categories=Category_tb.objects.all()
    return render(request, "product.html", {"ca": categories})

def productaction(request):
    name = request.POST["name"]
    price = request.POST['price']
    details = request.POST['details']
    stock = request.POST['stock']
    seller_id = request.session['sellerid']
    category = request.POST['category']
    if len(request.FILES)>0:
        img = request.FILES['image']
    else:
        img="no pic"

    product = product_table(
        name=name,
        price=price,
        details=details,
        stock=stock,
        seller_id_id=seller_id,
        category_id_id=category,
        image=img
    )
    product.save()
    messages.add_message(request,messages.INFO,"product added successfully")
    return redirect("product")

def viewproduct(request):
    sellerid=request.session["sellerid"]
    product=product_table.objects.filter(seller_id=sellerid)
    return render(request,"viewproduct.html",{'view':product})

def editproduct(request,id):
    product=product_table.objects.filter(id=id)
    categories=Category_tb.objects.all()
    return render(request,"editproduct.html",{'view':product,'ca':categories})

def editproductaction(request):
    id=request.POST['id']
    pro=product_table.objects.filter(id=id)
    name = request.POST["name"]
    price = request.POST['price']
    details = request.POST['details']
    stock = request.POST['stock']
    seller_id = request.session['sellerid']
    category = request.POST['category']
    if len(request.FILES)>0:
        img = request.FILES['image']
    else:
        img=pro[0].image
    pr=product_table.objects.get(id=id)
    pr.image=img
    pr.save()
    product = product_table.objects.filter(id=id).update(
        name=name,
        price=price,
        details=details,
        stock=stock,
        seller_id_id=seller_id,
        category_id_id=category,
    )
    messages.add_message(request,messages.INFO,"product updated successfully")
    return redirect("viewproduct")

def deleteproduct(request,id):
    user=product_table.objects.filter(id=id).delete()
    return redirect("viewproduct")  

def orderdetails_seller(request):
    seller_id=request.session['sellerid']
    details=product_table.objects.filter(seller_id=seller_id)
    orderitem=oderitems_table.objects.filter(productid_id__in=details)
    ordertable=order_table.objects.filter(id__in=orderitem)
    return render(request,"orderdetails_seller.html",{'view':ordertable})

def details_seller(request,id):
    seller_id=request.session['sellerid']
    details=product_table.objects.filter(seller_id=seller_id)
    orderitem=oderitems_table.objects.filter(productid_id__in=details,order_id_id=id)
    ordertable=order_table.objects.filter(id=id)
    return render(request,"details_seller.html",{'view':ordertable,'views':orderitem})

def orderstatus(request,id):
    order_table.objects.filter(id=id).update(status="approve")
    return redirect("orderdetails_seller")
def orderstatus_reject(request,id):
    order_table.objects.filter(id=id).update(status="reject")
    return redirect("orderdetails_seller")

def trackorder(request,id):
    user=order_table.objects.filter(id=id)
    return render(request,"trackorder.html",{'view':user})
    
def trackorderaction(request):

    id=request.POST['id']
    details= request.POST["details"]
    date=datetime.date.today()
    time=datetime.datetime.now().strftime("%H:%M")

    detail_s=tracking_table(orderid_id=id,
                            date=date,
                            time=time,
                            details=details)
    
    detail_s.save()
    return redirect("orderdetails_seller")

def changepassword_seller(request):
    return render (request,"changepassword_seller.html")

def changepasswordaction(request):
    sellerid=request.session['sellerid']
    
    oldpassword=request.POST['oldpass']
    newpassword=request.POST['newpass']
    conformpassword=request.POST['conformpass']
    s_id=seller_table.objects.filter(id=sellerid)

    if (s_id[0].password==oldpassword): 
    
        if newpassword == conformpassword:
              seller_table.objects.filter(id=sellerid).update(password=newpassword)
              messages.add_message(request,messages.INFO,"password changed") 
              return render(request,"seller_home.html")
        else:  
             messages.add_message(request,messages.INFO,"password does not match")  
             return redirect(changepassword_seller)  
 
    else:
        messages.add_message(request,messages.INFO,"old password is not equal to newpassword")
        return redirect(changepassword_seller)  