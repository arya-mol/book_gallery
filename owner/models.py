from django.db import models

# Create your models here.


books=[
   {"id": 100,"book_name":"randamoozham","author":"mt","price":480,"copies":250},
    {"id":101,"book_name": "aarachar", "author": "meera", "price": 580, "copies": 250},
    {"id":102,"book_name": "the alchemist", "author": "paulo", "price": 780, "copies": 250},
    {"id":103,"book_name": "rainrising", "author": "nirupama", "price": 1000, "copies": 250},
    {"id":104,"book_name": "indhuleka", "author": "chandhu menon", "price": 280, "copies": 250},
    {"id":105,"book_name": "pazhassy", "author": "mt", "price": 580, "copies": 350},

]

class Books(models.Model):
    book_name=models.CharField(max_length=120,unique=True)
    author=models.CharField(max_length=120)
    price=models.PositiveIntegerField(default=50)
    copies=models.PositiveIntegerField(default=10)
    active_status=models.BooleanField(default=True)
    image=models.ImageField(upload_to="images",null=True,blank=True)

    def __str__(self):
        return self.book_name
# print all book details availabile under 600
# books=Books.objects.filter(price__lt=600)
# books

# print all book details whoes price range 400 to 500
# books=Books.objects.filter(price__gt=400,price__lt=500)
# books


# print indulekha details
# book=Books.objects.get(id=5)
# book
# print(book.book_name,book.author_name,book.price,book.copies)

# print all book name whoes copies>30
# books=Books.objects.filter(copies__gt=30)
# books

# print count for copies>30
# books=Books.objects.filter(copies__gt=30).count()
#books

# print all inactive books
# books=Books.objects.filter(active_status=False)
# books

# print inactive book names
# booknames=Books.objects.filter(active_status=False).values("book_name")
# booknames


# create a new application location
# create a model districts with fields dist_name,population,first dose vaccination rate,second dose vaccination rate