from django import forms
from my apptwo.models import User

class User_form(forms.ModelForm):
    
    #generates form fields based on the models class
    class Meta:
        model = User
        fields = '__all__'