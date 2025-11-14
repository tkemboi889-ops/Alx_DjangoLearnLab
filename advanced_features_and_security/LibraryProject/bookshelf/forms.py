

from django import forms

class ContactForm(forms.Form):
    # This defines a text box for the name
    name = forms.CharField(max_length=100) 
    
    # This defines an input field specifically for email addresses
    email = forms.EmailField() 
    
    # This defines a large text area for the message
    message = forms.CharField(widget=forms.Textarea)