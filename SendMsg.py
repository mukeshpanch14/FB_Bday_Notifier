from twilio.rest import Client

class SendMsg(object):
    def __init__(self,message,mobileno):
        self.message=message
        self.mobileno=mobileno
    
    def SendMessage(self):
        account_sid = "AC771e278df6a3ab92af76aaceab0855f1"
        auth_token = "8968237e4ba957f9ef3d7819f6073afe"
        
        client = Client(account_sid, auth_token)
        
        client.api.account.messages.create(
            to=self.mobileno,
            from_="+12062036452",
            body=self.message+"-panch")
            
            