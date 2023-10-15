from django.shortcuts import render

# Create your views here.
def index(request):
    dict_content = {'myhello':'Hello developers from me!'}
    return render(request, 'first_app/index.html', context= dict_content)