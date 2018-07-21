import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'Company.settings')

import django
django.setup()


from company.models import User

from faker import Faker 



fk=Faker()

def user_dat(N=10):

    for entry in range(N):
        full_name=fk.name().split(" ")

        name1=full_name[0]
        name2=full_name[1]

        user_mail=fk.email()
    
        person=User.objects.get_or_create(
            
            First_Name=name1,
            Last_Name=name2,
            Email=user_mail
            
            )
    

if __name__ == '__main__':
    print ("Generating user data")
    user_dat(100)
    print("User details succesfully added to the database")