import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path #similar to os.path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Lynn Mitchell'
email['to'] = 'code7sandbox@gmail.com'
email['subject'] = 'Python Email'


# email.set_content('This email was sent with Python!')
email.set_content(html.substitute({'name': 'Name Namerson'} ), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    # start server
    smtp.ehlo()
    # ttls is encryption
    smtp.starttls()
    # dummy email
    smtp.login('code7sandbox@gmail.com', 'CodeEntry!==false')
    smtp.send_message(email)
    print('it worked')