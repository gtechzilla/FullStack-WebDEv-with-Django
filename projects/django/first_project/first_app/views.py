from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    my_dict={'Insert_me':"This is what was inserted"}
    return render(request,'first_app/index.html',context=my_dict)