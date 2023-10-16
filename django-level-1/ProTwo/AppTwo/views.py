from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User

# Create your views here.
def index(request):
    return HttpResponse('<em>My Second App</em>')

def help(request):
    dict_value ={'helpmessage':'Help Page!'}
    return render(request, 'AppTwo/index.html',context= dict_value)

def user(request):
    users = User.objects.order_by('first_name')
    dict_content = {'users': users}
    return render(request, 'AppTwo/user.html',context= dict_content)