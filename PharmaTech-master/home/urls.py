from django.contrib import admin
from django.urls import path , include
from  .import views 
from .views import AppointmentTemplateView , ManageAppointmentTemplateView
from home.controller import authview, cart, wishlist, checkout , order
 

urlpatterns = [
    path('', views.index, name="home") ,
    path('appointment/',AppointmentTemplateView.as_view() , name="appointment"),
    path('manage-appointment/',ManageAppointmentTemplateView.as_view() , name="manage-appointment"),
    path("collection/",views.collection , name="collection"),
    path("collection/<str:slug>",views.collectionview, name="collectionview"),
    path('collection/<str:cate_slug>/<str:prod_slug>',views.productview, name="productview"),
 

    path("register/",authview.register, name="register"),
    path("login/",authview.loginpage, name="loginpage"),
    path("logout/",authview.logoutpage , name="logout"),
    path('product-list', views.productlistAjax),
    path('searchproduct',views.searchproduct, name="searchproduct"),
    path('searchproduct',views.searchproduct, name="searchproduct"),
    path('profile',views.profile, name="profile"),

    path('cart/', cart.viewcart, name="cart"),
    path('add-to-cart', cart.addtocart , name="addtocart"),
    path('update-cart', cart.updatecart, name="updatecart"),
    path('deletet-cart-item',cart.deletecartitem, name='deletet-cart-item'),
    
    path('wishlist',wishlist.index, name="wishlist"),
    path('add-to-wishlist',wishlist.addtowishlist,name="addtowishlist"),
    path('delete-wishlist-item',wishlist.deletewishlistitem,name="deletewishlistitem"),

    path('checkout',checkout.index, name="checkout"),
    path('place-order',checkout.placeorder, name="placeorder"),
    path('proceed-to-pay',checkout.razorpaycheck),
    path('my-orders',order.index,name="myorders"),
    path('view=order/<str:t_no>',order.vieworder,name="orderview"),
    
    
    path("about/",views.about,name="about") ,
    path("blog/",views.blog,name="blog") ,
    path("cart/",views.cart,name="cart"),


   
    # path("my-orders",order.index,name="myorders"),
    # path("view-order.<str:t_no>",order.vieworder,name="orderview")
]