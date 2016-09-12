# Django Encryption Webapp

This is a pet project of [dhcrain.com](https://dhcrain.com/), please do not think that this an absolutely secure way of communicating, I am still learning, and __this is a work in progress.__

This allows a user to encrypt a text message and email the encrypted message and then send an SMS text with the key to someone.

In an effort to be secure, messages are only written to the database temporarily. Sessions are used to display confirmation of encryption and the decoded message. The data expires after 10 seconds.  

However, sent emails are in the outbox of the email account you used and, in the Twilio logs.


## To use:
1. Set up Python 3 virtual environment.  
2. `git clone https://github.com/dhcrain/encryption_website.git`  
3. `cd encryption_website`  
4. `pip install -r requirements.txt`  
5. Email Setup
    * At the bottom of settings.py
    * Email address and password, you may run into trouble if you have two factor activated.
6. SMS setup
    * Get free [Twilio](https://www.twilio.com/try-twilio) account, you will need:
    * In views.py or in environment settings
    * Account SID (twilio_account_sid)
    * Auth Token (twilio_auth_token)
    * Twilio Number (twilio_number)

7. `python manage.py migrate`
8. `python manage.py runserver`  
9. Go to http://127.0.0.1:8000/ in your web browser and get started
