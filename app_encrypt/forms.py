from django import forms
from django.utils.translation import ugettext_lazy as _


class EncryptForm(forms.Form):

    email = forms.EmailField(required=True,
                             help_text=_("Email Address to send encrypted message")
                             )
    message = forms.CharField(widget=forms.Textarea)
    phone = forms.CharField(required=True,
                            help_text=_("Phone number to text secret key")
                            )


class DecryptForm(forms.Form):

    encrypted_message = forms.CharField(widget=forms.Textarea)
    key = forms.CharField(required=True,
                            help_text=_("Exactally as it appears")
                            )
