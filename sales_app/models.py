from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User_model(AbstractUser):
    is_customer = models.BooleanField(default = False)
    is_seller = models.BooleanField(default = False)

class Customer(models.Model):
    user = models.ForeignKey(User_model, on_delete = models.CASCADE, related_name = "customers")
    name = models.CharField(max_length = 50)
    phone_number = models.CharField(max_length = 100)
    email = models.EmailField()
    status1 = models.BooleanField(default = 0)

    def __str__(self):
        return self.name

class Seller(models.Model):
    user = models.ForeignKey(User_model, on_delete = models.CASCADE, related_name = "sellers")
    name = models.CharField(max_length = 50)
    phone_number = models.CharField(max_length = 100)
    email = models.EmailField()
    status2 = models.BooleanField(default = 0)

    def __str__(self):
        return self.name


class mobileproduct(models.Model):
    seller = models.ForeignKey(Seller,on_delete = models.CASCADE, related_name = 'mobileproduct')
    name = models.CharField(max_length=250)
    brand = models.CharField(max_length=250)
    price = models.IntegerField()
    description = models.TextField()
    image=models.FileField(upload_to = 'documents/')

class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE, related_name = 'cart_customer')
    product = models.ForeignKey(mobileproduct, on_delete = models.CASCADE, related_name = "cart_product")
    status = models.IntegerField(default = 0)

class Buy(models.Model):
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE, related_name = 'buy_cart')
    quantity = models.IntegerField()
    adress = models.TextField()
    phone = models.CharField(max_length = 100)
    amount = models.IntegerField()

class Pay(models.Model):
    buy = models.ForeignKey(Buy, on_delete = models.CASCADE, related_name='pay_buy')
    card_number = models.CharField(max_length = 16)
    cvv = models.CharField(max_length = 3)
    expiry_date = models.DateField()

class Feedback(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name = "feedback_customer")
    date = models.DateField(auto_now = True)
    subject = models.CharField(max_length = 250)
    feedback = models.TextField()
    reply = models.TextField(null = True, blank = True)











