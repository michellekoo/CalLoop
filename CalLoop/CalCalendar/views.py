from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib import messages

def index(request):
	return render_to_response("index.html", context_instance=RequestContext(request,{}))

def user_home(request):
	context_dict = {}
	context_dict["courses"] = Subject.objects.filter(user=request.user)
	context_dict["assignments"] = Assignment.objects.filter(user=request.user)
	return render_to_response("user_home.html", context_instance=RequestContext(request,context_dict))

def user_auth(request):
	username = request.GET.get('Username', '0')
	password = request.GET.get('Password', '1')
	print(username)
	print(password)
	user = authenticate(username=username, password=password)	if user and user.is_active:
	if user and user.is_active:
		request.user = user
		return user_home(request)
	else:
		response = render_to_response("index.html", context_instance=RequestContext(request,{}))
		messages.add_message(request, "Invalid username or password")
		return response