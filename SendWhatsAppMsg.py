from twilio.rest import Client 
 
# account_sid = 'AC771e278df6a3ab92af76aaceab0855f1' 
# auth_token = '8968237e4ba957f9ef3d7819f6073afe' 
# client = Client(account_sid, auth_token) 
 
# message = client.messages.create( 
#                               from_='whatsapp:+14155238886',  
#                               body='Your appointment is coming up on {{July 21}} at {{3PM}}',      
#                               to='whatsapp:+918280041455' 
#                           ) 
 
# print(message.sid)




class SendWhatsAppMsg(object):
    def __init__(self,message,mobileno):
        self.message=message
        self.mobileno=mobileno
    
    def SendMessage(self):
        account_sid = "AC771e278df6a3ab92af76aaceab0855f1"
        auth_token = "8968237e4ba957f9ef3d7819f6073afe"
        print("Suceess")
        client = Client(account_sid, auth_token)
        
        if self.message=='No Birthdays Today':
        	client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body=self.message,      
                              to='whatsapp:'+self.mobileno
                          ) 
        else:
        	client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body=self.message+'\n'+'\n'+'_Call Them Immediately_',      
                              to='whatsapp:'+self.mobileno
                          ) 