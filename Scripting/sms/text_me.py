from twilio.rest import Client 
from dotenv import load_dotenv
load_dotenv()
import os

account_sid = os.getenv('ACCOUNT_SID') 
auth_token = os.getenv('AUTH_TOKEN') 
client = Client(account_sid, auth_token) 

print(auth_token)
 
message = client.messages.create( 
                              from_= os.getenv('PHONE_NUMBER_FROM') ,  
                              body='.env Test',      
                              to= os.getenv('PHONE_NUMBER_TO') 
                          ) 
 
print(message.sid)