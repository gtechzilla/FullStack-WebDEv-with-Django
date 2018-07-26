from django import forms

class FormName(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    text=forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False,widget=forms.HiddenInput)

    #function to check for the presence of bots filling out our forms
    #syntax of the function is 'clean_"name of your field" '
    def clean_botcatcher(self):

        #uses the cleaned_data attribute of the Form class
        botcatcher = self.cleaned_data['botcatcher']

        #The condition to be flagged
        if len(botcatcher) > 0:
            raise forms.ValidationError("Found A Bot")

        return botcatcher