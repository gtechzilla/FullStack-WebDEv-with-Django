from django.conf.urls import url
from company import views

urlpatterns = [
    url(r'^$',views.users,name='user_page')

]