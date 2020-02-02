from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class':"form-control",  'id':"name", 'placeholder':"Your Name"}))
    email = forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':"form-control",  'id':"email", 'placeholder':"Your Email"}))
    subject = forms.CharField(required=True, max_length=120, widget=forms.TextInput(attrs={'class':"form-control",  'id':"subject", 'placeholder':"Your Subject"}))
    number = forms.CharField(required=True, max_length=100, widget=forms.TextInput(attrs={'class':"form-control",  'id':"number", 'placeholder':"Your Number"}))
    message = forms.CharField(
        required=True,
        widget=forms.Textarea(attrs={'class':"form-control",  'id':"message", 'placeholder':"Your Message", 'cols':"30", 'rows':"10"})
    )

