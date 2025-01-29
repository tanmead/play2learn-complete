from django import forms

class ContactUsForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(
        widget=forms.Textarea(attrs={"rows": 5, "cols": 20}),
        help_text='Enter your message here.'
    )
