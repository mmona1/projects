from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=200)
    limit = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255)
    discription = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Add default=None
    img = models.ImageField(upload_to="uploads/images" ,null=True,blank=True)
 

    def __str__(self):
        return self.title





# class Reservation(models.Model):
#     name = models.CharField(max_length=100)
#     phone_number = models.CharField(max_length=20)
#     email = models.EmailField()
#     persons = models.IntegerField()
#     reservation_date = models.DateField()


class Booking(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField()
    persons = models.IntegerField()
    reservation_date = models.DateField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name







class Product_Category(models.Model):
    name = 	models.CharField( max_length =100 )

    def __str__(self):
        return self.name
  
    
class Product(models.Model):
    content_type=(
        ('burger','Burger'),
        ('pizza','Pizza'),
        ('pasta' ,'Pasta'),
        ('fries','Fries')
    ) 
    title = models.CharField( max_length=500,null=True)
    subtitle = models.CharField(max_length=500,null=True)
    description = models.TextField(null=True)
    product_category = models.ForeignKey(Product_Category,on_delete=models.CASCADE ,null=True)
    content_type = models.CharField(max_length=200,choices=content_type,default="")
    price = models.DecimalField(decimal_places=0, max_digits=8,)
    discounted_price = models.DecimalField(max_digits=5, decimal_places=0, default="0")
    offer_percentage = models.IntegerField(default=0)  # New field for offer in %
    product_image = models.ImageField( upload_to ='static/images',null=True )
    
   

    def offer_price(self):
        discount = self.price * self.offer_percentage / 100
        return self.price - discount
    
    
    
class shipping(models.Model):
    full_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    pin_code = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    # You can add more fields as needed, such as user, date, etc.

    def __str__(self):
        return f"Order for {self.full_name}"



class CartItem(models.Model):
    order = models.ForeignKey(shipping, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
          return f'Item {self.product.title} (x{self.quantity}) for Order {self.order.id}'
    
    
class user_order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # UserID as Foreign Key
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    shipping_details = models.ForeignKey(shipping, on_delete=models.CASCADE, null=True, blank=True)

    def _str_(self):
        return f'user_order{self.id} by User {self.user.username} - Subtotal: ${self.subtotal}'