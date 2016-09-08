# Django Encryption Webapp

This allows a user to encrypt a text message and email the encrypted message and then send an SMS text with the key to someone.

In an effort to be secure, no messages are written to the database. Sessions are used to display confirmation of encryption and the decoded message. The data is deleted from the session when it ends (browser is closed).  

This is a pet project of dhcrain.com, please do not think that this an absolutely secure way of communicating.

## To use:
Set up Python 3 virtual environment.  
`git clone https://github.com/dhcrain/encryption_website.git`  
`cd encryption_website`  
`pip install -r requirements.txt`  
`python manage.py runserver`  
Go to http://127.0.0.1:8000/ in your web browser
