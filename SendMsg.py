from twilio.rest import Client

class SendMsg(object):
    def __init__(self,message,mobileno):
        self.message=message
        self.mobileno=mobileno
    
    def SendMessage(self):
        account_sid = "account_sid"
        auth_token = "auth_token"
        
        client = Client(account_sid, auth_token)
        
        client.api.account.messages.create(
            to=self.mobileno,
            from_="+Twillio Number",
            body=self.message+"-panch")
            
            
