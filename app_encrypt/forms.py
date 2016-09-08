from django import forms
from django.utils.translation import ugettext_lazy as _


class EncryptForm(forms.Form):

    email = forms.EmailField(required=True,
                             help_text=_("Email Address to send encrypted message")
                             )
    phone = forms.CharField(required=True,
                            help_text=_("Phone number to text secret key")
                            )
    message = forms.CharField(widget=forms.Textarea)


class DecryptForm(forms.Form):

    key = forms.CharField(required=True,
                          help_text=_("Exactally as it appears in your text")
                          )
    encrypted_message = forms.CharField(widget=forms.Textarea,
                                        help_text=_("Copy and paste directly from your email.")
                                        )
