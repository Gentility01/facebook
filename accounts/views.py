from django.shortcuts import render,redirect
from . import urls
from .forms import UserRegistrationForm, UserUpdateForm, profileUpdateForm
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import login,authenticate
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
def form(request):
    if request.method == 'POST':
        username =request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request,user)
            return redirect ('index')

        else:
            messages.error(request, 'ERROR: INCORRECT USER OR PASSWORD...')
            return redirect('form')  

    else:
         return render(request,('pages/form.html'))



def register(request):
    if request.method == 'POST':
        first_name =request.POST.get('first-name')
        last_name =request.POST.get('last-name')
        user_name =request.POST.get('user_name')
        email =request.POST.get('email')
        password =request.POST.get('password')
        confirmpassword =request.POST.get('confirmpassword')

        if password == confirmpassword :
            register_user = User.objects.create_user(username = user_name, password = password, email = email, first_name = first_name, last_name = last_name)

            
            register_user.save()
            return redirect('form')
        else:
            messages.error(request, 'ERROR: THE TWO PASSWORDS DOES NOT MATCH !!!')
            return render(request, "pages/register.html")    

    return render(request,('pages/register.html'))  



@login_required
def profile(request):  
    # pass the update forms into a variable
    # to populate this forms with the initial values pass the instance as an argument
    # attatch the post method for security purposes
    if request.method == 'POST': 
        userupdateform = UserUpdateForm(request.POST, instance = request.user)
        profileupdateform = profileUpdateForm(request.POST, request.FILES, instance = request.user.profile)

        # saving the forms
        if userupdateform.is_valid() and profileupdateform.is_valid():
            userupdateform.save()
            profileupdateform.save()
            messages.success(request, f'Account updated succedfully')
            return redirect('login')  

    

    else:
        userupdateform = UserUpdateForm()
        profileupdateform = profileUpdateForm()
    
    
    #create a context for the forms and pass the contex to the profile page
    context = {
        'userupdateform':  userupdateform,
        'profileupdateform': profileupdateform
    }
    
    # this page is to be shown only when user is succesfully logged in
    return render(request, 'pages/profile.html', context ) 



def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('form')      
