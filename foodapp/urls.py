from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static 
urlpatterns = [
        path('', views.index, name='home'),
        path('home/',views.style, name='style'),
        path('about/', views.about, name='about'),
        path('menu/', views.menu, name='menu'),
        path('book/', views.book, name='book'),
        path('cart/', views.view_cart, name='cart'),
        path('add_to_cart/', views.add_to_cart, name='add_to_cart'),
        path('view_cart/', views.view_cart, name='view_cart'),
        path('remove_from_cart/', views.remove_from_cart, name='remove_from_cart'),
        path('edit_cart_item/', views.edit_cart_item, name='edit_cart_item'),
        path('signup/', views.signup, name='signup'),
        path('login/', views.user_login, name='login'),
        path('logout/', views.user_logout, name='user_logout'),
        path('checkout/', views.checkout, name='checkout'),
        
       

        

        
       
       
   
        

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
