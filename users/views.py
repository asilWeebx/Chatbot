from django.shortcuts import render, redirect
from django_email_verification import send_email
# Create your views here.
from django.contrib.auth import get_user_model, logout
from django.contrib.auth.hashers import make_password, check_password
from users.models import User


def confirm_needed(request, id):
    user = User.objects.get(id=id)
    if user.is_active == True:
        return redirect('/login')
    else:
        return render(request, 'confirm_template.html')


def my_functional_view(request):
    message = ''
    if request.method == 'POST':

        username = request.POST['username']
        name = request.POST['name']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if len(username) < 6:
            message = 'Your username is too short'
        elif User.objects.filter(username=username):
            message = 'This username is already token'
        elif len(email) < 6:
            message = 'Please enter true email address'
        elif User.objects.filter(email=email):
            message = 'You have already an account according to your email address'
        elif len(password1) < 6:
            message = 'The password must contain 6 symbols'
        elif password1 != password2:
            message = "The password don't match"
        else:
            user = get_user_model().objects.create(first_name=name, username=username,
                                                   password=make_password(password1), email=email)
            user.is_active = False
            send_email(user)
            return redirect('confirm_needed',user.id)

    return render(request, 'signup.html', {"message": message})


def Logout(request):
    logout(request)
    return redirect('index')
