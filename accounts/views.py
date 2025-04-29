from profile import Profile
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User  
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponse, HttpResponseRedirect

def register(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        
        # Normalize email for consistency
        email = email.strip().lower() if email else ""
        
        print(f"Registration attempt - Email: {email}")
        
        if not email or not password1 or not password2:
            messages.error(request, "All fields are required.")
            return redirect("register")
        
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect("register")
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect("register")
        
        try:
            # Create a new user with the email as both username and email
            user = User.objects.create_user(username=email, email=email, password=password1)
            user.save()
            print(f"User created successfully: {email}")
            
            messages.success(request, "Account created successfully. You can now log in.")
            return redirect("login")
        except Exception as e:
            print(f"Error creating user: {str(e)}")
            messages.error(request, "An error occurred during registration. Please try again.")
            return redirect("register")
    
    return render(request, "accounts/register.html")

def login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        remember_me = request.POST.get("remember_me") == "on"
        
        # Normalize email for consistency
        email = email.strip().lower() if email else ""
        
        if not email or not password:
            messages.error(request, "Please enter both email and password.")
            return redirect("login")
        
        # Print debug info to server console
        print(f"Login attempt - Email: {email}, Remember me: {remember_me}")
        
        # Try direct authentication first (this might work in most cases)
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            auth_login(request, user)
            
            # Set session expiry based on remember me checkbox
            if remember_me:
                # Session will last for 2 weeks (14 days)
                request.session.set_expiry(1209600)
            else:
                # Session will expire when the user closes the browser
                request.session.set_expiry(0)
                
            messages.success(request, "Login successful.")
            print(f"Login successful for {email}")
            return redirect("/")
        
        # If direct authentication fails, try to find the user and debug
        try:
            user_obj = User.objects.get(email=email)
            print(f"User found with email {email}, username: {user_obj.username}")
            
            # Try again with the explicit username
            user = authenticate(request, username=user_obj.username, password=password)
            
            if user is not None:
                auth_login(request, user)
                
                # Set session expiry based on remember me checkbox
                if remember_me:
                    # Session will last for 2 weeks (14 days)
                    request.session.set_expiry(1209600)
                else:
                    # Session will expire when the user closes the browser
                    request.session.set_expiry(0)
                    
                messages.success(request, "Login successful.")
                print(f"Login successful for {email} using explicit username")
                return redirect("/")
            else:
                print(f"Authentication failed for user {email} - password mismatch")
                
                # For security in production, you would use a generic message
                # But for debugging, let's be specific
                messages.error(request, "Password is incorrect. Please try again.")
        except User.DoesNotExist:
            print(f"No user found with email {email}")
            messages.error(request, "No account found with this email address.")
        except Exception as e:
            print(f"Login error: {str(e)}")
            messages.error(request, "An error occurred during login. Please try again.")
        
        return redirect("login")
    
    return render(request, "accounts/login.html")

def reset_admin_password(request):
    """Development utility to reset an admin user's password (remove in production)"""
    if request.method == "POST":
        email = request.POST.get("email")
        new_password = request.POST.get("new_password")
        
        if not email or not new_password:
            messages.error(request, "Both email and new password are required")
            return render(request, "accounts/reset_password.html")
        
        try:
            user = User.objects.get(email=email)
            user.set_password(new_password)
            user.save()
            print(f"Password reset successful for {email}")
            messages.success(request, f"Password reset for {email} was successful. You can now login.")
            return redirect("login")
        except User.DoesNotExist:
            messages.error(request, "User with that email does not exist")
        except Exception as e:
            print(f"Error resetting password: {str(e)}")
            messages.error(request, "An error occurred while resetting password")
    
    return render(request, "accounts/reset_password.html")

# def login(request):
#     if request.method == 'POST':
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         user_obj = User.objects.filter(username = email)

#         if not user_obj.exists():
#             messages.warning(request, 'Account not found.')
#             return HttpResponseRedirect(request.path_info)


#         if not user_obj[0].profile.is_email_verified:
#             messages.warning(request, 'Your account is not verified.')
#             return HttpResponseRedirect(request.path_info)

#         user_obj = authenticate(username = email , password= password)
#         if user_obj:
#             login(request , user_obj)
#             return redirect('')

        

#         messages.warning(request, 'Invalid credentials')
#         return HttpResponseRedirect(request.path_info)


#     return render(request ,'accounts/login.html')


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

#         messages.success(request, 'An email has been sent on your mail.')
#         return HttpResponseRedirect(request.path_info)


#     return render(request ,'accounts/register.html')




# def activate_email(request , email_token):
#     try:
#         user = Profile.objects.get(email_token= email_token)
#         user.is_email_verified = True
#         user.save()
#         return redirect('/')
    
#     except Exception as e:
#         return HttpResponse('Invalid Email token')