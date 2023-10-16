from django import forms
from django.core import validators


#check name start with z
# def check_for_z(value):
#     if value[0].lower()!= 'z':
#         raise forms.ValidationError("Name needs to start with z")


class FormName(forms.Form):
    # name =forms.CharField(validators=[check_for_z])
    name =forms.CharField()
    email=forms.EmailField()
    verify_email = forms.EmailField(label='Enter your email again: ')
    #Specify type field is textarea with widget forms.Textarea
    text= forms.CharField(widget=forms.Textarea)
    #check for bot
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput
                                 ,validators=[validators.MaxLengthValidator(0)])
    
    # def clean_botcatcher(self):
    #     botcatcher= self.cleaned_data['botcatcher']
    #     if len(botcatcher)>0:
    #         raise forms.ValidationError("GOTCHA BOT!")
    #     return botcatcher

    #Custom model validation
    def clean(self):
        #return all clean data
        all_clean_data = super().clean()
        email = all_clean_data['email']
        verify_mail= all_clean_data['verify_email']

        if email != verify_mail:
            raise forms.ValidationError("Make Sure Emails Match")