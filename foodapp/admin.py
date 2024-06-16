from django.contrib import admin

# Register your models here.
from . models import Post,Category,Product,Product_Category
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Product_Category)



   

