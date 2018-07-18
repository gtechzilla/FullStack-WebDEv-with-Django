##CONFIGURES THE PROJECT SETTINGS
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')

##SETTING UP DJANGO
import django
django.setup()

##FAKE POULATION SCRIPT
import random
from first_app.models import AccessRecord,Topic,Webpage
from faker import Faker

fakegen = Faker() 

topics=['Search','MarketPlace','News','Entertainment']

#function to create a topic
def add_topic():
    #get_or_create() method returns a tuple of which we pick the first index
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range (N):

        #first assign it a topic
        top=add_topic()

        #generate the fake data
        fake_url=fakegen.url()
        fake_date = fakegen.date()
        fake_name =fakegen.company()

        #creating a new webpage entry
        webpg=Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        #creating a fake access record for the page
        accs_rcrd=AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
    print("Populating script")
    populate(20)
    print("Populating Complete")
