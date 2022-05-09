from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from customer.models import Orders,Profile

class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))

    class Meta:
        model=User
        fields=["username","first_name","last_name","email","password1","password2"]
        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"})

        }

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())


class OrderForm(forms.ModelForm):
    class Meta:
        model=Orders
        fields=["address"]
        widgets={
            "address":forms.Textarea(attrs={"class":"form-control"})
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=("user",)




# class FeedbackForm(forms.Form):
#     product_name=forms.CharField()
#     feedback=forms.CharField()
#
#
# class RegistrationForm(forms.Form):
#     first_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form_control"}))
#     last_name=forms.CharField(widget=forms.TextInput(attrs={"class":"form_control"}))
#     email=forms.CharField(widget=forms.EmailInput(attrs={"class":"form_control"}))
#     phone=forms.CharField(widget=forms.TextInput(attrs={"class":"form_control"}))
#     username=forms.CharField(widget=forms.TextInput(attrs={"class":"form_control"}))
#     password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form_control"}))
#
#     def clean(self):
#         cleaned_data=super().clean()
#         phone=(cleaned_data.get("phone"))
#         if len(phone)!=10:
#             message="invalid phone number"
#             self.add_error("phone",message)
#
# class LoginForm(forms.Form):
#     username=forms.CharField(widget=forms.TextInput(attrs={"class":"form_control"}))
#     password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form_control"}))
#

