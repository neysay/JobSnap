'''
Created on Jul 19, 2015

@author: jacobmelvin
'''
from django import forms
from .models import SignUp
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_forms.bootstrap import FieldWithButtons, StrictButton


class SimpleForm(forms.Form):
    email = forms.EmailField(label = "")
    
    helper = FormHelper()
    helper.form_method = 'POST'
    #helper.label_class = 'col-lg-2'
    #helper.field_class = 'col-lg-10'
    #helper.form_class = 'form-horizontal'
    #helper.add_input(Submit('submit','Get Early Access',css_class='btn-primary'))
    helper.layout = Layout(
                           FieldWithButtons('email',Submit('submit','Get Early Access',css_class='btn-primary'))
                           #FieldWithButtons('email',StrictButton("GO!"))
                           )


class SignUpForm(forms.ModelForm):
    def __init__(self, *args, **kwargs): 
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        #self.css_class = "rule"
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        #helper.label_class = 'col-lg-2'
        #helper.field_class = 'col-lg-10'
        #helper.form_class = 'form-horizontal'
        #helper.add_input(Submit('submit','Get Early Access',css_class='btn-primary'))
        self.helper.layout = Layout(
                               FieldWithButtons('email',Submit('submit','Get Early Access',css_class='btn-primary'))
                               #FieldWithButtons('email',StrictButton("GO!"))
                               )
    
    class Meta:
        model = SignUp
        fields = ['email']
        labels = {'email': ""}
        widgets = {'email': forms.TextInput(attrs={'placeholder': 'Enter Email'})}
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, provider = email.split("@")
        domain, extension = provider.split('.')
        
        return email
