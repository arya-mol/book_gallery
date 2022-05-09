from django.shortcuts import render,HttpResponse,redirect
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView,DeleteView
from owner.models import books,Books
from owner.forms import BookForm,OrderProcessForm
from django.urls import reverse_lazy
from customer.decorators import owner_permission_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from customer.models import Orders
from django.core.mail import send_mail

# Create your views here.
@method_decorator(owner_permission_required,name="dispatch")
class BookList(ListView):
    model = Books
    context_object_name = 'books'
    template_name = 'book_list.html'


# class BookList(View):
    # def get(self,request,*args,**kwargs):
    #     books = Books.objects.all()
    #     context={"books":books}
    #     return render(request,"book_list.html",context)


@method_decorator(owner_permission_required,name="dispatch")
class AddBook(CreateView):
    model = Books
    form_class = BookForm
    template_name = 'book_add.html'
    success_url = reverse_lazy('listbook')


# class AddBook(View):
#     def get(self,request,*args,**kwargs):
#         form=BookForm()
#         return render(request,"book_add.html",{"form":form})
#     def post(self,request,*args,**kwargs):
#         print(request.POST)
#         form=BookForm(request.POST,files=request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request,"book has been added")
#             # name = form.cleaned_data.get("book_name")
#             # author = form.cleaned_data.get("author")
#             # price = form.cleaned_data.get("price")
#             # copies = form.cleaned_data.get("copies")
#             # book = Books(book_name=name, author=author, price=price, copies=copies)
#             # book.save()
#             return redirect("addbook")
#         else:
#             context={"form":form}
#             messages.error(request,"book adding failed")
#             return render(request, "book_add.html",context)




    #     bookname=request.POST["bk_name"]
    #     author=request.POST["bk_author"]
    #     price=request.POST["bk_price"]
    #     copies=request.POST["bk_copies"]

@method_decorator(owner_permission_required,name="dispatch")
class BookDetail(DetailView):
    model = Books
    context_object_name = 'book'
    template_name = 'book_detail.html'
    pk_url_kwarg = "id"


# class BookDetail(View):
#     def get(self,request,*args,**kwargs):
#         id=kwargs["id"]
#         book=Books.objects.get(id=id)
#         # book=[book for book in books if book["id"]==id][0]
#         context={"book":book}
#         return render(request,"book_detail.html",context)


@method_decorator(owner_permission_required,name="dispatch")
class BookChange(UpdateView):
    model = Books
    template_name = "book_edit.html"
    form_class = BookForm
    pk_url_kwarg = "id"
    success_url = reverse_lazy("listbook")





# class BookChange(View):
#     def get(self,request,*args,**kwargs):
#         print(kwargs)
#         id=kwargs["id"]
#         book=Books.objects.get(id=id)
#         # book = [book for book in books if book["id"] == id][0]
#         # form=BookEdit(initial={"book_name":book["book_name"],"author":book["author"],"price":book["price"],"copies":book["copies"]})
#         form=BookForm(instance=book)
#         return render(request,"book_edit.html",{"form":form})
#
#     def post(self,request,*args,**kwargs):
#         id=kwargs["id"]
#         book=Books.objects.get(id=id)
#         form=BookForm(request.POST,instance=book,files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("listbook")


@method_decorator(owner_permission_required,name="dispatch")
class BookDelete(DeleteView):
    template_name = "book_delete.html"
    pk_url_kwarg = "id"
    success_url = reverse_lazy("listbook")
    model = Books



# class BookDelete(View):
#     def get(self,request,*args,**kwargs):
#         id=kwargs["id"]
#         book=Books.objects.get(id=id)
#         book.delete()
#         return redirect("listbook")



class OwnerDashBoard(ListView):
    model = Orders
    template_name = "owner_dashboard.html"
    def get(self,request,*args,**kwargs):
        new_orders=self.model.objects.filter(status="orderplaced")
        context={"n_orders":new_orders}
        return render(request,self.template_name,context)




class OrderDetails(DetailView):
    model = Orders
    template_name = "order_detail.html"
    context_object_name = "order"
    pk_url_kwarg = "o_id"


class OrderProcessView(UpdateView):
    model = Orders
    pk_url_kwarg = "id"
    template_name = "order_process.html"
    form_class = OrderProcessForm
    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        e_delivery_date=form.cleaned_data.get("expected_delivery_date")
        send_mail(
            'bookorderconformation',
            'your order will be delivered on'+str(e_delivery_date),
            'aryamolchanjaplackal@gmail.com',
            ['angelsankar@gmail.com'],
            fail_silently=False,
        )
        return super().form_valid(form)





