from django.shortcuts import render,redirect
from home.forms import SignupForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from home.models import File
def signup(request):
	form=SignupForm(request.POST)
	if form.is_valid():
		user=form.save(commit=False)
		user.first_name=form.cleaned_data.get('first_name')
		user.last_name=form.cleaned_data.get('last_name')
#		user.email=form.cleaned_data.get('email_address')
		user.save()
		auth_login(request,user)
		return redirect('home')
	else:
		form=SignupForm()
	return render(request,'signup.html',{'form':form})
@login_required
def profile(request,slug):
	user=User.objects.filter(username=slug)
	user=user[0];
	file=File.objects.filter(uploaded_by=user)
	return render(request,'profile.html',{'users':user ,'file':file})
