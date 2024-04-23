from django import forms
from django.contrib.auth.forms import UserCreationForm

from sales_app.models import  Login,Customer, Seller


class LoginRegister(UserCreationForm):
    username=forms.CharField()
    password1 = forms.CharField(label="password",widget=forms.PasswordInput)
    password2= forms.CharField(label="confirm password",widget=forms.PasswordInput)

    class Meta:
        model=Login
        fields=('username','password1','password2')

class CustomerRegister(forms.ModelForm):

    class Meta:
        model=Customer
        fields=("__all__")
        exclude=("user","status1")


class SellerRegister(forms.ModelForm):
    class Meta:
        model=Seller
        fields=('__all__')
        exclude=("user","status2")












