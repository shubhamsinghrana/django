from django import  forms
from django.core import validators

# def check_for_z(value):
#     if value[0] != 'z':
#         raise forms.ValidationError("need to start from z")


class FormName(forms.Form):
    # name=forms.CharField(validators=[check_for_z])
    name=forms.CharField()
    email=forms.EmailField()
    verify_email=forms.EmailField(label='Enter ypur email again:')
    
    text =forms.CharField(widget=forms.Textarea)
    def clean(self):
        all_clean_data= super().clean()
        email =all_clean_data['email']
        vmail =all_clean_data['verify_email']

        if email !=vmail:
            raise forms.ValidationError("Make sure email matches")


    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])


    # def clean_botcatcher(self):
    #     botcatcher =self.cleaned_data['botcatcher']
    #     if len(botcatcher)>0:
    #         raise forms.ValidationError("GOTCHA BOT!")
    #     return botcatcher
