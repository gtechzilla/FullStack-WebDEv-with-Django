from django import forms

#django class that handles form validation
from django.core import validators

class FormName(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    verify_email=forms.EmailField(label='Retype your email')
    text=forms.CharField(widget=forms.Textarea)

    #clean method is used for cleaning form at once
    def clean(self):

        #super().clean grabs all the cleaned data from the form
        all_cleaned_data = super().clean()

        '''The clean method from supers store the cleaned data as a dictionary
        to get a certain field you call the key of the dictionary'''
        email=all_cleaned_data['email']
        vmail= all_cleaned_data['verify_email']

        if email !=vmail:
            raise forms.ValidationError("Your Emails do not match")

