from django import forms
from django.utils.translation import ugettext_lazy as _


class ContactForm(forms.Form):

    email = forms.EmailField(required=True,
                             help_text=_("Email Address to send encrypted message")
                             )
    message = forms.CharField(widget=forms.Textarea)
    phone = forms.CharField(required=True,
                            help_text=_("Phone number to text secret key")
                            )
