from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index(request):
    if request.user.is_authenticated:
    	return redirect('home:index')
    else:
	    if request.method == "POST":

	    	user = request.POST['username']
	    	passwd = request.POST['password']

	    	user = authenticate(request, username = user, password=passwd)
	    	if user is not None:
	    		login(request, user)
	    		# messages.success(request, 'Login Berhasil !! Selamat Datang di Aplikasi POS')
	    		return redirect('home:index')
	    	else:
	    		messages.info(request, 'Incorect Username or Password')
	    		return redirect('index')

	    return render(request,'login.html',{'title' : 'Login Page'})



def getlogout(request):
	logout(request)
	return redirect('index')