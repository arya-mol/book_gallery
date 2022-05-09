from django.urls import path
from customer import views

urlpatterns=[
    path('book/home',views.CustomerHome.as_view(),name="custhome"),
    path('accounts/signup',views.SignupView.as_view(),name="signup"),
    path('',views.SigninView.as_view(),name="signin"),
    path('accounts/signout',views.sign_out,name="signout"),
    path('customers/carts/add/<int:id>',views.AddToCart.as_view(),name="addtocart"),
    path('customers/carts/items/',views.CartItems.as_view(),name="cartitems"),
    path("customers/carts/items/remove/<int:id>",views.RemoveCartItem.as_view(),name="removeitem"),
    path("customers/orders/add/<int:p_id>/<int:c_id>",views.OrderCreate.as_view(),name="order_create"),
    path("customers/orders",views.MyOrdersView.as_view(),name="myorders"),
    path("customers/orders/remove/<int:id>",views.cancell_order,name="cancelorder"),
    path("profiles/add",views.ProfileView.as_view(),name="profile"),
    path("profiles/views",views.ViewMyProfile.as_view(),name="viewprofile")

]