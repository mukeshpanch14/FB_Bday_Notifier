from twilio.rest import Client 
 
# account_sid = 'account_sid' 
# auth_token = 'auth_token' 
# client = Client(account_sid, auth_token) 
 
# message = client.messages.create( 
#                               from_='whatsapp:+Twillio Number',  
#                               body='Your appointment is coming up on {{July 21}} at {{3PM}}',      
#                               to='whatsapp:+918280041455' 
#                           ) 
 
# print(message.sid)




class SendWhatsAppMsg(object):
    def __init__(self,message,mobileno):
        self.message=message
        self.mobileno=mobileno
    
    def SendMessage(self):
        account_sid = "account_sid"
        auth_token = "auth_token"
        print("Suceess")
        client = Client(account_sid, auth_token)
        
        if self.message=='No Birthdays Today':
        	client.messages.create( 
                              from_='whatsapp:+Twillio Number',  
                              body=self.message,      
                              to='whatsapp:'+self.mobileno
                          ) 
        else:
        	client.messages.create( 
                              from_='whatsapp:+Twillio Number',  
                              body=self.message+'\n'+'\n'+'_Call Them Immediately_',      
                              to='whatsapp:'+self.mobileno
                          ) 
