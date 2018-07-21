from django.shortcuts import render
from company.models import User

# Create your views here.

def home(request):
    return render(request,'company_app/home.html')


def users(request):
    user_list=User.objects.order_by('First_Name')
    user_data={'User_Details':user_list}
    return render(request,'company_app/users.html',context=user_data)