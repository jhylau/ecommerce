
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from django.core import serializers
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def signup(request):
    return render(request, 'members/signup.html', {})

def login(request):
	return render(request, 'members/signup.html', {})

def register(request):
    user = User.objects.create_user(request.POST['username'],request.POST['email'],request.POST['pwd'])
    user.save()
    print request.POST
    return HttpResponse("register" + str(user.id))

def test(request):
    # data = serializers.serialize("json", <query set> User.objects.all())
    return HttpResponse(data, content_type='application/json')


