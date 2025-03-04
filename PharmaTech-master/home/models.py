from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import datetime
import os
from django.http import request
# Create your models here.

class Appointment(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    request = models.TextField(blank=True)
    sent_date = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)
    accepted_date = models.DateField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.first_name
    
    class Meta:
        ordering = ["-sent_date"]

def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime, original_filename)
    return os.path.join('uploads/', filename)
    
class Category(models.Model):
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True) 
    description = models.TextField(max_length=500, null=False, blank=False) 
    status = models.BooleanField(default=False, help_text="0=default, 1=Hidden")
    trending = models.BooleanField(default=False, help_text="0=default, 1=Trending")
    meta_title= models.CharField(max_length=150, null=False, blank=False)
    meta_keywords= models.CharField(max_length=150, null=False, blank=False)
    meta_description= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    

     
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.CharField(max_length=150, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    product_image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    small_description = models.CharField(max_length=250, null=False, blank=False)
    quantity = models.IntegerField(null=False, blank=False) 
    description = models.TextField(max_length=500, null=False, blank=False)
    original_price = models.FloatField(null=False, blank=False) 
    selling_price = models.FloatField(null=False, blank=False)
    status = models.BooleanField(default=False, help_text="0=default, 1=Hidden")
    trending = models.BooleanField(default=False, help_text="0=default, 1=Trending")
    tag = models.CharField(max_length=150, null=False, blank=False)
    meta_title= models.CharField(max_length=150, null=False, blank=False)
    meta_keywords= models.CharField(max_length=150, null=False, blank=False)
    meta_description= models.DateTimeField(auto_now_add=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
   


class Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_qty = models.IntegerField(null=False,blank=False)
    created_at = models.DateField(auto_now_add=True)
 

class Order(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        fname = models.CharField(max_length=150, null=False)
        lname = models.CharField(max_length=150, null=False)
        email = models.CharField(max_length=150, null=False)
        phone = models.CharField(max_length=150, null=False)
        address = models.TextField(null=False)
        city = models.CharField(max_length=150, null=False)
        state = models.CharField(max_length=150, null=False)
        country = models.CharField(max_length=150, null=False)
        pincode = models.CharField(max_length=150, null=False)
        total_price = models.FloatField(null=False)
        payment_mode = models.CharField(max_length=150, null=False)
        payment_id = models.CharField(max_length=250, null=False)
        orderstatuses = (
            ('pending','pending'),
            ('Out For shipping','Out For shipping'),
            ('completed','completed'),
        )
        status = models.CharField(max_length=150,choices=orderstatuses, default='pending')
        message = models.TextField(null=True)
        tracking_no = models.CharField(max_length=150, null=True)
        created_at = models.DateField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.FloatField(null=False)
    quantity = models.IntegerField(null=False)

    def __str__(self):
        return '{} {}'.format(self.order.id, self.order.tracking_no)

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    phone = models.CharField(max_length=50,null=False)
    address = models.TextField(null=False)
    image = models.ImageField(default='default.jpg', upload_to = '_profile_pics_')
    city = models.CharField(max_length=150,null=False)
    state = models.CharField(max_length=150,null=False)
    country = models.CharField(max_length=150,null=False)
    pincode = models.CharField(max_length=150,null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} Profile'



        
# class ProfilePage(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.ImageField(default='default.jpg', upload_to='profile_pics')
#     def __str__(self):
#         return f'{self.user.username} Profile'
#     # Override the save method of the model
#     def save(self):
#         super().save()

#         img = Image.open(self.image.path) # Open image

#         # resize image
#         if img.height > 300 or img.width > 300:
#             output_size = (300, 300)
#             img.thumbnail(output_size) # Resize image
#             img.save(self.image.path) # Save it again and override the larger image
