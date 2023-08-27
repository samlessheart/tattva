from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='Your Name', max_length=100)
    email_id = forms.EmailField()
    Phone = forms.CharField(label='Your Phone No.')
    Message = forms.CharField(widget=forms.Textarea)
    