import smtplib
from email.message import EmailMessage


email = EmailMessage()
email['from'] = 'Lynn Mitchell'
email['to'] = 'code7sandbox@gmail.com'
email['subject'] = 'Python Email'


email.set_content('This email was sent with Python!')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    # start server
    smtp.ehlo()
    # ttls is encryption
    smtp.starttls()
    smtp.login('code7sandbox@gmail.com', 'CodeEntry!==false')
    smtp.send_message(email)
    print('it worked')