from django.urls import path
from api import views


urlpatterns=[
    path('book/all',views.BooksView.as_view()),
    path('book/<int:id>',views.BooksDetails.as_view())
]