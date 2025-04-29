# from django.shortcuts import get_object_or_404, render
# from django.shortcuts import redirect
# from django.contrib.auth import login 
# from .models import Coffee
# from .models import CartItem
# from django.contrib import messages
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate 
# from django.http import HttpResponseRedirect,HttpResponse

# def home(request):
#     coffee=Coffee.objects.all()
#     return render(request,'home.html',{'coffee':coffee})

# def about(request):
#     return render(request, 'about.html')


# def register(request):
#     if request.method=='POST':
#         form=UserRegistrationForm(request.POST)
#         if form.is_valid():
#             user=form.save(commit=False)
#             user.set_password(form.cleaned_data['password1'])
#             user.save()
#             # login(request,user)
#             return redirect('home')    
#     else:
#         form=UserRegistrationForm()
    
#     return render(request,'register.html',{'form':form})


# def search_view(request):
#     query = request.POST.get('search_query', '').strip()  # Get the query from the form
#     if query:  # If query is not empty
#         coffee_results = Coffee.objects.filter(name__contains=query)  # Adjust the filter based on your model
#     else:
#         coffee_results = None  # No results if no query
    
#     return render(request, 'search-view.html', {
#         'query': query,
#         'coffee': coffee_results,
#     })
    
# def buy_now(request,slug):
#     coffee=get_object_or_404(Coffee,slug=slug)
#     print(coffee) # Adjust query as needed
#     return render(request, 'buy_now.html', {'coffee': coffee})

# def register(request):

#     if request.method == 'POST':
#         first_name = request.POST.get('first_name')
#         last_name = request.POST.get('last_name')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user_obj = User.objects.filter(username = email)

#         if user_obj.exists():
#             messages.warning(request, 'Email is already taken.')
#             return HttpResponseRedirect(request.path_info)

#         print(email)

#         user_obj = User.objects.create(first_name = first_name , last_name= last_name , email = email , username = email)
#         user_obj.set_password(password)
#         user_obj.save()

#         messages.success(request, 'you have sign up.')
#         return HttpResponseRedirect(request.path_info)


#     return render(request ,'register.html')

# def login_page(request):
    
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user_obj = User.objects.filter(username = email)

        # if not user_obj.exists():
        #     messages.warning(request, 'Account not found.')
        #     return HttpResponseRedirect(request.path_info)


        # if not user_obj[0].profile.is_email_verified:
        #     messages.warning(request, 'Your account is not verified.')
        #     return HttpResponseRedirect(request.path_info)

#         user_obj = authenticate(username = email , password= password)
#         if user_obj:
#             login(request , user_obj)
#             return redirect('')
#         if user_obj is not None:
#             login(request, user_obj)
#             return redirect('dashboard')  # Redirect to a valid URL name
#         else:
#             return render(request, 'login.html', {'error': 'Invalid credentials'})
#     return render(request, 'login.html')

        

#         # messages.warning(request, 'Invalid credentials')
#         # return HttpResponseRedirect(request.path_info)


#     # return render(request ,'login.html')


# def add_to_cart(request, coffee_id):
#     coffee = get_object_or_404(Coffee, pk=coffee_id)

#     # Add the coffee item to the cart for the logged-in user
#     if request.user.is_authenticated:
#         cart_item, created = CartItem.objects.get_or_create(user=request.user, coffee=coffee)

#         # Optionally, you can increase the quantity if the item is already in the cart
#         if not created:
#             cart_item.quantity += 1
#             cart_item.save()

#     return redirect('cart_detail')

# def cart_detail(request):
#     if request.user.is_authenticated:
#         # Fetch cart items from the database for authenticated users
#         cart_items = CartItem.objects.filter(user=request.user)
#     else:
#         # Retrieve cart items from the session for unauthenticated users
#         cart_items = request.session.get('cart', {}).values()

#     return render(request, 'cart_detail.html', {'cart_items': cart_items})



# def download_cart(request):
#     if request.user.is_authenticated:
#         cart_items = CartItem.objects.filter(user=request.user)
#         total_price = sum(item.coffee.price * item.quantity for item in cart_items)

        # Create cart summary as a text file
#         content = "Cart Summary\n\n"
#         for item in cart_items:
#             content += f"Item: {item.coffee.name}\n"
#             content += f"Category: {item.coffee.category}\n"
#             content += f"Quantity: {item.quantity}\n"
#             content += f"Price: ${item.coffee.price * item.quantity}.00\n"
#             content += "-" * 20 + "\n"

#         content += f"\nTotal Price: ${total_price}.00\n"

#         # Return file as HTTP response
#         response = HttpResponse(content, content_type="text/plain")
#         response["Content-Disposition"] = 'attachment; filename="cart_summary.txt"'
#         return response
#     else:
#         return HttpResponse("You must be logged in to download your cart.", content_type="text/plain")
    
    
    
# def cart_history(request):
#     if request.user.is_authenticated:
#         cart_items = CartItem.objects.filter(user=request.user)

#         # Add total price for each cart item
#         cart_data = [
#             {
#                 "coffee": item.coffee,
#                 "quantity": item.quantity,
#                 "total_price": item.coffee.price * item.quantity,
#             }
#             for item in cart_items
#         ]

#         # Calculate the overall total price
#         total_price = sum(item["total_price"] for item in cart_data)

#         return render(request, "cart_history.html", {"cart_items": cart_data, "total_price": total_price})
#     else:
#         return render(request, "cart_history.html", {"cart_items": [], "total_price": 0})


# Create y
# def add_to_cart(request, slug):
#     product = get_object_or_404(Product, slug=slug)
    
#     cart, created = Cart.objects.get_or_create(user=request.user, is_active=True)
    
#     # Check if the product already exists in the cart
#     cart_item, created = CartItems.objects.get_or_create(cart=cart, product=product)
    
#     if not created:  # If item already exists, increase quantity
#         cart_item.quantity += 1
#         cart_item.save()
# cart = Cart.objects.filter(user=request.user, is_active=True).first()
    
#     # Fetch cart items and calculate total price
#     cart_items = CartItems.objects.filter(cart=cart) if cart else []

#     total_price = sum(item.total_price for item in cart_items)
    
#     return render(request, 'cart/cart.html', {
#         'cart_items': cart_items,
#         'total_price': total_price,
#     })





