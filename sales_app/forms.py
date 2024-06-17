from django import forms
from django.contrib.auth.forms import UserCreationForm
from sales_app.models import User_model, Customer, Seller, Product, Cart, Pay, Feedback


class User_form(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(label = "password", widget = forms.PasswordInput)
    password2 = forms.CharField(label="confirm password", widget = forms.PasswordInput)

    class Meta:
        model = User_model
        fields = ('username', 'password1', 'password2')

class CustomerRegister(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ("__all__")
        exclude = ("user", "status1")



class SellerRegister(forms.ModelForm):
    class Meta:
        model = Seller
        fields = ('__all__')
        exclude = ("user", "status2","admin_approval_status")


class mobile_product_form(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('__all__')
        exclude = ('seller',)

class dateinput(forms.DateInput):
    input_type = 'date'

class pay_form(forms.ModelForm):
# for overwriting the form field linked to the model field'date'
# in the Payment model.
    expiry_date = forms.DateField(widget = dateinput(attrs = {'style':'background-color:white;'}))
    card_number = forms.CharField(widget = forms.TextInput(attrs = {'style': 'background-color:white;'}))
    cvv = forms.CharField(widget = forms.TextInput(attrs = {'style': 'background-color:white;'}))
    class Meta:
        model = Pay
        fields = ('__all__')
        exclude = ('buy',)
        # for single field in exclude comma(,) is needed

class customer_feedback_form(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('subject','feedback')





























