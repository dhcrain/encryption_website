# Django Encryption Webapp

This allows a user to encrypt a text message and email the encrypted message and then send an SMS text with the key to someone.

In an effort to be secure, no messages are written to the database. Sessions are used to display confirmation of encryption and the decoded message. The data is deleted from the session when it ends (browser is closed).  

This is a pet project of [dhcrain.com](https://dhcrain.com/), please do not think that this an absolutely secure way of communicating, I am still learning, and this is a work in progress.

## To use:

Get free [Twilio](https://www.twilio.com/try-twilio) account, you will need:

* Account SID
* Auth Token
* Twilio Number
* In views.py or in environment settings

Enter email info, currently set up for Gmail:

* Email address and password, you may run into trouble if you have two factor activated.
* At the bottom of settings.py

### Then:
1. Set up Python 3 virtual environment.  
2. `git clone https://github.com/dhcrain/encryption_website.git`  
3. `cd encryption_website`  
4. `pip install -r requirements.txt`  
5. `python manage.py runserver`  
6. Go to http://127.0.0.1:8000/ in your web browser and get started
