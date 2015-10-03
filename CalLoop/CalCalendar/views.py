from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, world!")

def user_home(request):
	context_dict = {}
	context_dict["courses"] = Subject.objects.filter(user=request.user)
	context_dict["assignments"] = Assignment.objects.filter(user=request.user)
	return render_to_response("user_home.html", context_instance=RequestContext(request,context_dict))

def user_auth(request):
	username = request.GET.get('Username', '0')
	password = request.GET.get('Password', '1')
	user = authenticate(username=username, password=password)
	if user and user.is_active:
		ret = HttpRequest()
		ret.user = user
		ret.path = r'^user_home/'
		return ret
	else:
		return