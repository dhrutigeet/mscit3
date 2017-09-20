from django.shortcuts import render
from django.http import HttpResponse
from django.http import response
from django.template import loader
from .models import mscit
from .models import ExampleModel
from stud.forms import ImageUploadForm
from stud.forms import loginForm
from django.http import HttpResponseForbidden
import sqlite3
# Create your views here.
#def index(request):
	#return HttpResponse("<b>Hello welcome to College</b>")
	
def list(request):
	request.session['usernm']='dhruti'
	#response.set_cookie("eid","abc@rediff.com")
	#e=request.COOKIES['eid']
	return render(request,'stud/list.html',{})
	
def about(request):
	return render(request,'stud/about.html',{})
def contact(request):
	return render(request,'stud/contact.html',{})
def courses(request):
	r=mscit.objects.all()
	return render(request,'stud/courses.html',{"data":r})
	
def insert(request):
	cn=sqlite3.connect("db.sqlite3")
	rs=cn.cursor()
	rs.execute("insert into stud_mscit values(9,'krupa','rkt') ")
	cn.commit()
	cn.close()
	return render(request,'stud/list.html',{})
	
def delete(request):
	cn=sqlite3.connect("db.sqlite3")
	rs=cn.cursor()
	rs.execute("delete from stud_mscit where id=9 ")
	cn.commit()
	cn.close()
	return render(request,'stud/list.html',{})	

def upload_pic(request):
	form=ImageUploadForm()
	'''if request.method == 'POST':
		form = ImageUploadForm(request.POST,request.FILES)
        if form.is_valid():
			m = ExampleModel.objects.get(pk=course_id)
			m.model_pic = form.cleaned_data['image']
			m.save()
            return HttpResponse('image upload success')'''
	return render(request,"stud/event.html",{"form":form})

def login(request):
	form=loginForm()
	return render(request,"stud/login.html",{"form":form})
def chklogin(request):
	form=loginForm()
	if request.method == 'POST':
		form=loginForm(request.POST)
		if form.is_valid():
			unm=request.POST.get('username')
			pwd=request.POST.get('password')
			response.set_cookie("user",unm)
			return render(request,'stud/disp.html',{})
	else:
		return render(request,'stud/list.html',{})
def disp(request):
	if 'user' in request.COOKIES:
		user=request.COOKIES['user']
	return render(request,'stud/disp.html',{'user':user})