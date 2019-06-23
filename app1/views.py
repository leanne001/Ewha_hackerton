from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
from .models import Profile


def home(request):
    return render(request, 'home.html')

# Create your views here.

def login(request):
    if request.method =="POST":
        userid = request.POST['ID']
        password = request.POST['password']
        user = auth.authenticate(request, userid=userid, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error' : 'userid or password is incorrect'})
    else:        
        return render(request, 'login.html')

def signup(request):
    
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try :
                user = User.objects.get(username=request.POST['ID'])
                return render(request, 'signup.html', {'error':'ID has already been used'})
            except User.DoesNotExist :
                user = User.objects.create_user(
                    username=request.POST['ID'], password=request.POST['password1'])
                    
                auth.login(request,user)
                user2 = User.objects.get(username=user.username)
                #profile.user = user

                user2.profile.studentid = request.POST['studentid']
                user2.profile.major = request.POST['major']
                user2.profile.contact = request.POST['contact']
                user2.profile.menu = request.POST['menu']
                user2.profile.save()
                return redirect('home')
        else:
            return render(request, 'signup.html', {'error':'Password must match'})
    else:
        return render(request, 'signup.html') #{'user':user, 'number':number, 'depart':depart, 'favor':favor}

def userlist(request):
    profile = Profile.objects
    return render(request, 'userlist.html', {'profiles' : profile})