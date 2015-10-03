from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
from django.http import HttpResponse

def index(request):
	return HttpResponse("Hello, world!")

def user_home(request):
	context_dict = {}
	context_dict["courses"] = Subject.objects.filter(user=request.user)
	context_dict["assignments"] = Assignment.objects.filter(user=request.user)
	return render_to_response("user_home.html", context_instance=RequestContext(request,context_dict))

