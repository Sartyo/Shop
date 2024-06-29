from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=50, required=True)
    email = forms.EmailField(label='Email', max_length=100, required=True)
    subject = forms.CharField(label='Subject', required=True)
    msg = forms.CharField(label='Message', required=True, widget=forms.Textarea)