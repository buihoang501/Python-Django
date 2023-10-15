from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<em>My Second App</em>')

def help(request):
    dict_value ={'helpmessage':'Help Page!'}
    return render(request, 'help/index.html',context= dict_value)