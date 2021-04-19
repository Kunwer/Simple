from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserUpdateForm
import pyrebase
from django.contrib.auth.models import User
from .models import Profile
config={
    "apiKey": "AIzaSyDcEdb_lBOs9m-XEP9W7zv9PIorCupBu5s",
    "authDomain": "simple-91dd0.firebaseapp.com",
    "databaseURL": "https://simple-91dd0-default-rtdb.firebaseio.com/",
    "projectId": "simple-91dd0",
    "storageBucket": "simple-91dd0.appspot.com",
    "messagingSenderId": "260826023789",
    "appId": "1:260826023789:web:7c82f5c42aac10a059fc64"
}
firebase=pyrebase.initialize_app(config)
authe = firebase.auth()
database=firebase.database()

@login_required
def home(request):
    users = Profile.objects.all()
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user.profile)
        if u_form.is_valid():
            u_form.save()
    else:
        u_form = UserUpdateForm(instance=request.user.profile)
    return render(request,'users/home.html',{'u_form':u_form,'users':users,'curr_user':request.user.username})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


def login(request):
    return render(request,'users/login.html')