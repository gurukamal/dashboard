from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth


# Create your views here.
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            print('invalid ')
    else:
        return render(request, 'accounts/login.html')


def register(request):
    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        qualification = request.POST['qualification']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                print('user exists')
            elif User.objects.filter(email=email).exists():
                print('email exists')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name,
                                                qualification=qualification)
                user.save()
                print('user created')
        else:
            return render(request, 'accounts/login.html')
