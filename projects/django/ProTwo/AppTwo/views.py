from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(requests):
    my_dict={'Help_Me':"How May We be of Assistance"}
    return render(requests,'help_app/help.html',context=my_dict)
