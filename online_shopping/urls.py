"""online_shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from site_admin import views as admin_view
from buyer import views as buyer_view
from seller import views as seller_view
from django.conf.urls.static import static
from django.conf import settings 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',admin_view.index,name="index"),
    path('admin_login/',admin_view.admin_login,name="admin_login"),
    path('loginaction/',admin_view.login_action,name="loginaction"),
    path('buyer_registration/',buyer_view.buyer_registration,name="buyer_registration"),
    path('registeraction/',buyer_view.registeraction,name="registeraction"),
    path('editinfo/',buyer_view.editinfo,name="editinfo"),
    path('editaction/',buyer_view.editaction,name="editaction"),
    path('sellerregisteration/',seller_view.sellerregistration,name="sellerregistration"),
    path('sellerregisteraction/',seller_view.sellerregisteraction,name="sellerregisteraction"),
    path('addcategory/',admin_view.addcategory,name="addcategory"),
    path('categoryaction/',admin_view.categoryaction,name="categoryaction"),
    path('sellereditinfo/',seller_view.sellereditinfo,name="sellereditinfo"),
    path('sellereditinfoaction/',seller_view.sellereditinfoaction,name="sellereditinfoaction"),
    path('viewseller/',admin_view.viewseller,name="viewseller"),
    path('statusapprove<int:id>/',admin_view.statusapprove,name="statusapprove"),
    path('statusreject<int:id>/',admin_view.statusreject,name="statusreject"),
    path('product/',seller_view.product,name="product"),
    path('productaction/',seller_view.productaction,name="productaction"),
    path('viewproduct/',seller_view.viewproduct,name="viewproduct"),
    path('editproduct<int:id>/',seller_view.editproduct,name="editproduct"),
    path('editproductaction/',seller_view.editproductaction,name="editproductaction"),
    path('deleteproduct<int:id>/',seller_view.deleteproduct,name="deleteproduct"),
    path('buyerview/',buyer_view.buyerview,name="buyerview"),
    path('addtocart<int:id>/',buyer_view.addtocart,name="addtocart"),
    path('cartaction/',buyer_view.cartaction,name="cartaction"),
    path('viewcart/',buyer_view.viewcart,name="viewcart"),
    path('deleteitem<int:id>/',buyer_view.deleteitem,name="deleteitem"),
    path('orderaction/',buyer_view.orderaction,name="orderaction"),
    path('payment<int:id>/',buyer_view.payment,name="payment"),
    path('paymentaction/',buyer_view.paymentaction,name="paymentaction"),
    path('viewdetails/',buyer_view.viewdetails,name="viewdetails"),
    path('details<int:id>/',buyer_view.details,name="details"),
    path('cancelorder<int:id>/',buyer_view.cancelorder,name="cancelorder"),
    path('orderdetails_seller/',seller_view.orderdetails_seller,name="orderdetails_seller"),
    path('details_seller<int:id>/',seller_view.details_seller,name="details_seller"),
    path('orderstatus<int:id>/',seller_view.orderstatus,name="orderstatus"),
    path('orderstatus_reject<int:id>/',seller_view.orderstatus_reject,name="orderstatus_reject"),
    path('trackorder<int:id>/',seller_view.trackorder,name="trackorder"),
    path('trackorderaction/',seller_view.trackorderaction,name="trackorderaction"),
    path('trackingdetails<int:id>/',buyer_view.trackingdetails,name="trackingdetails"),
    path('changepassword/',buyer_view.changepassword,name="changepassword"),
    path('passwordaction/',buyer_view.passwordaction,name="passwordaction"),
    path('changepassword_seller/',seller_view.changepassword_seller,name="changepassword_seller"),
    path('changepasswordaction/',seller_view.changepasswordaction,name="changepasswordaction"),
    path('username/',admin_view.username,name="username"),
    path('forgotpassword/',admin_view.forgotpassword,name="forgotpassword"),
    path('forgotpassword1/',admin_view.forgotpassword1,name="forgotpassword1"),
    path('forgotpassword2/',admin_view.forgotpassword2,name="forgotpassword2"),
    path('logout/',admin_view.logout,name="logout"),
    


]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)