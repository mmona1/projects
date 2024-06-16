from multiprocessing import AuthenticationError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post,Category,Product_Category,Product,shipping,user_order,CartItem,Booking
from django.http import JsonResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, authenticate,logout
from django.contrib import messages







# Create your views here.
def index(request):
    top = Post.objects.filter(category_id=4)
    carosel= Post.objects.filter(category_id=6)
    client = Post.objects.filter(category_id=2)
    about = Post.objects.filter(category_id=1)
    carosel = Post.objects.filter(category_id=3)
    offer = Post.objects.filter(category_id=5)
    product_category = Product_Category.objects.get(name='Menu')
    products = Product.objects.filter(product_category=product_category)
    content_type = Product.objects.values('content_type') .distinct()
    cart_count = get_cart_count(request)  
    data = {'client' : client ,
            'about': about,
            'carosel':carosel,
            'offer': offer, 
            'top':top,
            'carosel':carosel, 
            "product_category":product_category,
            "products":products,
            "content_type":content_type,
            "cart_count": cart_count
            }
    return render(request, 'index.html',data)



def style(request):
    top = Post.objects.filter(category_id=4)
    toparea = {'top':top }
    return render(request, 'style.html',toparea)




def about(request):
    about = Post.objects.filter(category_id=1)
    
    alldata = {'about': about }
    return render(request, 'about.html',alldata )



# for menu page
def menu(request):
    
     # products with 'menu' category
    product_category = Product_Category.objects.get(name='Menu')
    products = Product.objects.filter(product_category=product_category)
    content_type = Product.objects.values('content_type') .distinct()
    cart_count = get_cart_count(request)
    context ={
        "product_category":product_category,
        "products":products,
        "content_type":content_type,
        "cart_count": cart_count
    }
    return render(request ,'menu.html',context)



def book(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        persons = request.POST.get('persons')
        reservation_date = request.POST.get('reservation_date')

        # Save the data to the database
        booking = Booking(name=name, phone_number=phone_number, email=email, persons=persons, reservation_date=reservation_date)
        booking.save()
        return JsonResponse({'success': True, 'message': 'Booking successful!'})
    
    else:
        return render(request, 'book.html',)
    
     





#for keeping the cart count 

# for showing item count on navbar cart icon 
def get_cart_count(request):
    cart = request.session.get('cart', {})
    return sum(cart.values())




def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = [{'id': key, 'quantity': value} for key, value in cart.items() if key.isdigit()]  # Filter out non-integer IDs
    product_ids = [item['id'] for item in cart_items]
    products = Product.objects.filter(id__in=product_ids)
    cart_count = get_cart_count(request)
    


    for item in cart_items:
        product = products.get(id=item['id'])
        item['product'] = product
        item['total_price'] = product.price * item['quantity']

    subtotal = sum(item['total_price'] for item in cart_items)
    subtotal_formatted = "{:.2f}".format(subtotal)

    context = {
        'cart_items': cart_items,
        'cart_count':cart_count,
        'subtotal': subtotal_formatted
    }
    return render(request, 'cart.html', context)




def add_to_cart(request):
    if request.method == "POST":
        item_id = request.POST.get('item_id')
        quantity = int(request.POST.get('quantity', 1))

        # Add to the cart in session
        cart = request.session.get('cart', {})
        if item_id in cart:
            cart[item_id] += quantity
        else:
            cart[item_id] = quantity

        request.session['cart'] = cart
 
        # Calculate the total cart count
        cart_count = sum(cart.values())

        return JsonResponse({
            'success': True,
            'cart_count': cart_count
        })

    return JsonResponse({'success': False, 'error': 'Invalid method'})






#for removing cart item
def remove_from_cart(request):
    if request.method == "POST":
        item_id = request.POST.get('item_id')
        cart = request.session.get('cart', {})

        if item_id in cart:
            del cart[item_id]
            request.session['cart'] = cart
            return JsonResponse({'success': True, 'message': 'Item removed successfully!'})

        return JsonResponse({'success': False, 'message': 'Item not found in cart!'})

    return JsonResponse({'success': False, 'message': 'Invalid method'})

#for editing cart item

def edit_cart_item(request):
    if request.method == "POST":
        item_id = request.POST.get('item_id')
        new_quantity = int(request.POST.get('new_quantity'))

        cart = request.session.get('cart', {})
        if item_id in cart:
            cart[item_id] = new_quantity
            request.session['cart'] = cart

            product = Product.objects.get(id=item_id)
            updated_total_price = product.price * new_quantity

            return JsonResponse({'success': True, 'message': 'Quantity updated successfully!','updated_total_price': "{:.2f}".format(updated_total_price)})

        return JsonResponse({'success': False, 'message': 'Item not found in cart!'})

    return JsonResponse({'success': False, 'message': 'Invalid method'})





def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('view_cart')  # Redirect to your home page after successful sign-up
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})




def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('view_cart')  # Redirect to your home page
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})




def user_logout(request):
    logout(request)
    return redirect('home')






def order_address(request):
    if request.method == 'POST':
        full_name = request.POST['full_name']
        address = request.POST['address']
        city = request.POST['city']
        phone = request.POST['phone']
        pin_code = request.POST['pin_code']
        
        # Create a new order instance and save it to the database
        order = shipping(
            full_name=full_name,
            address=address,
            city=city,
            phone=phone,
            pin_code=pin_code,
        )
        order.save()

        # You can also associate this order with a user if your application has user authentication

        # Redirect to a thank you page or order confirmation page
        return redirect('view_cart')  # Replace 'order_confirmation' with your actual URL name

    # Handle GET request or render the form
    return render(request, 'order_form.html') 

def checkout(request):
    cart = request.session.get('cart', {})
    cart_items = [{'id': key, 'quantity': value} for key, value in cart.items()]
    products = Product.objects.filter(id__in=cart.keys())
    cart_count = get_cart_count(request)
    
    for item in cart_items:
        product = products.get(id=item['id'])
        item['product'] = product
        item['total_price'] = product.price * item['quantity']

    subtotal = sum(item['total_price'] for item in cart_items)

    subtotal_formatted = "{:.2f}".format(subtotal)
    context = {
         'cart_items': cart_items,
         'cart_count': cart_count,
         'subtotal': subtotal_formatted,
      }

    if request.method == 'POST':
        full_name = request.POST['full_name']
        address = request.POST['address']
        city = request.POST['city']
        phone = request.POST['phone']
        pin_code = request.POST['pin_code']
        

        # Create an order instance and save it to the database
        order = shipping(
            full_name=full_name,
            address=address,
            city=city,
            phone=phone,
            pin_code=pin_code,
        )
        order.save()

        # Create a user_order instance to associate it with the user and order 
        user_order_obj = user_order(
            user=request.user,  # Replace with the appropriate user object
            subtotal=subtotal,
            shipping_details=order,
        )
        user_order_obj.save()
        
        
        for item in cart_items:
            order_item = CartItem(
                order=order,
                product=item['product'],
                quantity=item['quantity'],
                total_price=item['total_price']
            )
            order_item.save()

        # Redirect to a thank you page or order confirmation page
      # Redirect to a thank you page or order confirmation page
        request.session['cart'] = {}
        response_data = {'success': True}
        return JsonResponse(response_data)
    
     # Replace 'order_confirmation' with your actual URL name

    # Handle GET request or render the form
    return render(request, 'order_summary.html',context) 
       
       
       
       
       
       
       
       
       
