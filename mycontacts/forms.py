from django import forms
from .models import Contact

class AddForm(forms.Form):
    
    class Meta:
        model = Contact
        fields = ('name', 'relation', 'phone', 'email',)

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    relation = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=20)
    email = forms.EmailField()