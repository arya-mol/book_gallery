from django.urls import path
from owner import views

urlpatterns=[
    path('books/all',views.BookList.as_view(),name="listbook"),
    path('books/add',views.AddBook.as_view(),name="addbook"),
    path('books/<int:id>', views.BookDetail.as_view(), name="bookdetail"),
    path('books/change/<int:id>', views.BookChange.as_view(),name="bookedit"),
    path('books/remove/<int:id>', views.BookDelete.as_view(), name="deletebook"),
    path("dashboard",views.OwnerDashBoard.as_view(),name="dashboard"),
    path("orders.<int:o_id>",views.OrderDetails.as_view(),name="orderdetail"),
    path("orders/process/<int:id>",views.OrderProcessView.as_view(),name="orderprocess")

]





