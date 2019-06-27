from django.shortcuts import render,redirect
from django.http import Http404
from .models import File,Stream
from .forms import UploadForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
@login_required
def home(request):
	user=request.user
	files=File.objects.all()
	stream=Stream.objects.all()
	return render(request,'home.html',{'files':files, 'user':user, 'stream':stream})

def upload(request):
	form=UploadForm(request.POST,request.FILES)
	user=request.user
	if form.is_valid():
		file=form.save(commit=False)
		file.uploaded_by=user
		file.save()
		return redirect('home')
	else:
		form=UploadForm()
	return render(request,'upload.html',{'form':form})

def allfiles(request,slug):
	stream=Stream.objects.all()
	for value in stream:
		if (slug==value.name):
			files=File.objects.filter(branch=slug)
			return render(request,'allfiles.html',{'files':files,'slug':slug})
	raise Http404('No branch named '+ slug)
