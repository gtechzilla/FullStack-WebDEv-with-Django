from django import forms

#django class that handles form validation
from django.core import validators

def check_for_gerald(value):
    if value=='gerald':
        raise forms.ValidationError('You cant use This name')

class FormName(forms.Form):
    name=forms.CharField(validators=[check_for_gerald])
    email=forms.EmailField()
    text=forms.CharField(widget=forms.Textarea)

    #just add the validators attribute to the field u want to validate
    botcatcher = forms.CharField(
                                    required=False,
                                    widget=forms.HiddenInput,
                                    validators=[validators.MaxLengthValidator(0)]
                                )

