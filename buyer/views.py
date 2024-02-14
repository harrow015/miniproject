from django.shortcuts import render,redirect
import datetime
from buyer.models import *
from seller.models import *
from django.contrib import messages
# Create your views here.
def buyer_registration(request):
    return render(request,"register.html")
def registeraction(request):
    name=request.POST['name']
    address=request.POST['address']
    gender=request.POST['gender']
    place=request.POST['place']
    username=request.POST['username']
    password=request.POST['password']
    mobile=request.POST['mobile']
    dob=request.POST['dob']
    user=register_table(Name=name,Address=address,Gender=gender,Place=place,Username=username,Password=password,DOB=dob,Mobile=mobile)
    user.save()
    messages.add_message(request,messages.INFO,"registration was successful")
    return redirect("buyer_registration")
def editinfo(request):
    id=request.session['userid']
    user=register_table.objects.filter(id=id)
    return render(request,'editinformation.html',{'view':user})
def editaction(request):
    id=request.POST['id']
    name=request.POST['name']
    address=request.POST['address']
    gender=request.POST['gender']
    place=request.POST['place']
    username=request.POST['username']
    mobile=request.POST['mobile']
    dob=request.POST['dob']
    user=register_table.objects.filter(id=id).update(Name=name,
                                                     Address=address,
                                                     Gender=gender,
                                                     Place=place,
                                                     Username=username,
                                                     DOB=dob,
                                                     Mobile=mobile)
    messages.add_message(request,messages.INFO,"user info updated successfully")
    return render(request,"userhome.html")
    
def buyerview(request):
    product=product_table.objects.all()
    return render(request,"buyerview.html",{'view':product})

def addtocart(request,id):
    product=product_table.objects.filter(id=id)
    return render(request,"cart.html",{'view':product}) 
def cartaction(request):
    productid=request.POST['id']  
    buyerid= request.session["userid"]
    shippingaddress=request.POST['address']
    phone=request.POST['mobile']
    quantity=request.POST['quanty']
    total=request.POST['total']
    stock=request.POST['stock'] 
    if int(stock)<int(quantity):
         messages.add_message(request,messages.INFO,"invalid quantity")
         return redirect(buyerview)
    else:
        user=cart_table(productid_id=productid,
                        buyerid_id=buyerid,
                        shipping_address=shippingaddress,
                        phone=phone,
                        quantity=quantity,
                        total=total)
        user.save()
    messages.add_message(request,messages.INFO,"oder placed successfully")
    return redirect(buyerview)
def viewcart(request):
    grandtotal=0
    buyerid=request.session['userid']
    cart=cart_table.objects.filter(buyerid_id=buyerid)
    for i in cart:
        total=i.total
        grandtotal=grandtotal+total
    if len(cart)<0:
         messages.add_message(request,messages.INFO,"cart is empty")
    else:
        return render(request,"viewcart.html",{'view':cart,"gtotal":grandtotal})
    
def deleteitem(request,id):
    buyerid=request.session['userid']
    grandtotal=0
    cart=cart_table.objects.filter(id=id).delete()
    carts=cart_table.objects.filter(buyerid_id=buyerid)
    for i in carts:
        total=i.total
        grandtotal=grandtotal+total
    if len(cart)<0:
         messages.add_message(request,messages.INFO,"cart is empty")
    else:
        return render(request,"viewcart.html",{'view':carts,"gtotal":grandtotal})

def orderaction(request):
    name=request.POST['name']
    address=request.POST['address']
    phone=request.POST['phone']
    buyerid=request.session['userid']
    grandtotal=request.POST['grandtotal']
    orderdate=datetime.date.today()
    ordertime=datetime.datetime.now().strftime("%H:%M")

    order=order_table(name=name,
                     address=address,
                     buyerid_id=buyerid,
                     phone=phone,
                     order_date=orderdate,
                     order_time=ordertime,
                     grandtotal=grandtotal)
    order.save()

    cart=cart_table.objects.filter(buyerid_id=buyerid)
    for i in cart:
        cartitem=cart_table.objects.filter(id=i.id)
        productid=cartitem[0].productid.id 
        quantity=cartitem[0].quantity
        stock=cartitem[0].productid.stock
        total=cartitem[0].total
        newstock=stock-quantity
        product=product_table.objects.filter(id=productid).update(stock=newstock)
        orderitem=oderitems_table(quantity=quantity,
                                  total=total,
                                  buyerid_id=buyerid,
                                  order_id_id=order.id,
                                  productid_id=productid

                                  
                                  )
        orderitem.save()
    messages.add_message(request,messages.INFO,"order placed successfully")
    return redirect ("payment",order.id)

def payment(request,id):
     id=order_table.objects.filter(id=id)     
     return render(request,"payment.html",{'views':id}) 
    
    
def paymentaction(request):    
    cardname=request.POST['cardname']
    cardnumber=request.POST['cardnumber']
    cvv=request.POST['cvv']
    expdate=request.POST['expdate']
    buyerid=request.session['userid']
    orderid=request.POST['orderid']
    
    pay=payment_table(cardname=cardname,
                      cardnumber=cardnumber,
                      cvv=cvv,
                      expiary_date=expdate,
                      buyerid_id=buyerid,
                      orderid_id=orderid)
    
    pay.save()
    messages.add_message(request,messages.INFO,"payment  successfull")
    return render(request,"userhome.html")

def viewdetails(request):
    buyerid=request.session['userid']
    details=order_table.objects.filter(buyerid_id=buyerid)
    return render(request,"viewdetails.html",{'view':details}) 

def details(request,id):
    orderdetails=order_table.objects.filter(id=id)
    buyerid=request.session['userid']
    orderid=oderitems_table.objects.filter(order_id_id=id,buyerid_id=buyerid)
    return render(request,"orderdetails.html",{'view':orderdetails,'views':orderid})

def cancelorder(request,id):
     order_table.objects.filter(id=id).update(status="canceled")
     return redirect('viewcart')

def trackingdetails(request,id):
    track=tracking_table.objects.filter(orderid_id=id)
    if len(track)<=0:
        messages.add_message(request,messages.INFO,"no tracking details found")
        return redirect("details")
    else:    
        return render(request,"trackorder_buyer.html",{'view':track})

def changepassword(request):
    return render(request,"changepassword.html")

def passwordaction(request):
    buyerid=request.session['userid']
    
    oldpassword=request.POST['oldpass']
    newpassword=request.POST['newpass']
    conformpassword=request.POST['conformpass']
    r_id=register_table.objects.filter(id=buyerid)

    if (r_id[0].Password==oldpassword): 
    
        if newpassword == conformpassword:
              register_table.objects.filter(id=buyerid).update(Password=newpassword)
              messages.add_message(request,messages.INFO,"password changed") 
              return render(request,"userhome.html")
        else:  
             messages.add_message(request,messages.INFO,"password does not match")  
             return redirect(changepassword)  
 
    else:
        messages.add_message(request,messages.INFO,"old password is not equal to newpassword")
        return redirect(changepassword)  