from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from CalCalendar.models import *

def index(request):
	return render_to_response("index.html", context_instance=RequestContext(request,{}))

def user_home(request):
	context_dict = {}
	context_dict["user"] = request.user
	context_dict["courses"] = Subject.objects.filter(user=request.user)
	context_dict["assignments"] = Assignment.objects.filter(user=request.user)
	return render_to_response("user_home.html", context_instance=RequestContext(request,context_dict))

def user_auth(request):
	if request.method == 'POST':
		username = request.POST.get('Username')
		password = request.POST.get('Password')
		user = authenticate(username=username,
			password=password)
		if user and user.is_active:
			login(request, user)
			return HttpResponseRedirect("/user_home/")
		else:
			return HttpResponse("/")
	return HttpResponseRedirect("/")

def new_account(request):
	return render_to_response("newaccount.html", context_instance=RequestContext(request,{}))

def sign_up(request):
	if request.method == 'POST':
		firstname = request.POST.get('First name')
		lastname = request.POST.get('Last name')
		email = request.POST.get('Email')
		username = request.POST.get('Username')
		password = request.POST.get('Password')
		re_enter_password = request.POST.get('Re-enter Password')

		if (password == re_enter_password):
			user = User.objects.create_user(username, email, password)
			user.last_name = lastname
			user.first_name = firstname
			user.save()
	return HttpResponseRedirect("/")
