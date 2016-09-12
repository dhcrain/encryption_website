# from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from app_encrypt.forms import EncryptForm, DecryptForm
from django.core.urlresolvers import reverse_lazy
from django.core.mail import send_mail
from cryptography.fernet import Fernet
from twilio.rest import TwilioRestClient
import os


class EncryptView(FormView):
    form_class = EncryptForm
    success_url = reverse_lazy('encrypt_template_view')
    template_name = 'encrypt.html'

    def form_valid(self, form):
        to_email = form.cleaned_data.get('email')
        # Convert to b
        msg = str.encode(form.cleaned_data.get('message'))
        # Genereate key
        key = Fernet.generate_key()
        f = Fernet(key)
        # Encrypt text
        encrypted_msg = f.encrypt(msg).decode()
        # Convert from b
        key_str = key.decode()
        # send email with encrypted text
        message = """
You have recived an encrypted message, go to {} to decrypt,
you should also get the secret key by another method.

<----------- Copy below this line ----------->
{}
<------- Stop copying above this line ------->

This is a side project of dhcrain.com
No guarantee of security
        """.format(self.request.build_absolute_uri('decrypt'), encrypted_msg)
        send_mail(
            subject="You have an ecrypted message",
            message=message,
            from_email=os.environ['email_username'],
            recipient_list=[to_email],
        )
        # send text with secret key
        twilio_account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
        twilio_auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
        twilio_number = os.environ.get('TWILIO_NUMBER')

        client = TwilioRestClient(twilio_account_sid, twilio_auth_token)
        to_phone = form.cleaned_data.get('phone')
        message = client.messages.create(body=key_str,
                                         to="+1{}".format(to_phone),
                                         from_=twilio_number)
        # add info to session data to display confirmation on next page.
        self.request.session['encoded_email'] = to_email
        self.request.session['encoded_phone'] = to_phone
        self.request.session.set_expiry(10)  # Data removed from DB after 10 sec
        return super().form_valid(form)


class EncryptTemplateView(TemplateView):
    template_name = 'encrypt_success.html'


class DecryptView(FormView):
    form_class = DecryptForm
    success_url = reverse_lazy('decoded_view')
    template_name = 'decrypt.html'

    def form_valid(self, form):
        key = form.cleaned_data.get('key')
        key = str.encode(key)
        f = Fernet(key)
        encrypted_msg = form.cleaned_data.get('encrypted_message')
        msg_b = str.encode(encrypted_msg)
        msg = f.decrypt(msg_b)
        # add info to session data to display confirmation on next page.
        self.request.session['decoded_msg'] = msg.decode()
        self.request.session.set_expiry(10)  # Data removed from DB after 10 sec
        return super().form_valid(form)


class DecodedView(TemplateView):
    template_name = "decrypt_success.html"
