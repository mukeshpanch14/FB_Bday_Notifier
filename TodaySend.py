import csv
import datetime
import SendMsg as SM
import SendWhatsAppMsg as SWM



class TodaySend(object):
	def __init__(self,csv_file,mobileno):
		self.csv_file=csv_file
		self.mobileno=mobileno
	def checkDateSend(self):	
		today=datetime.datetime.now().strftime("%m-%d")
		today4msg=datetime.datetime.now().strftime("%B %d")
		msg="*"+today4msg+" Birthdays Today:*"+'\n'+'\n'
		with open(self.csv_file,encoding="utf-8") as csvfile:
			reader=csv.DictReader(csvfile)
			for row in reader:
				if today==row['DATE'] and row!="":
					msg=msg+row['NAME']+'\n'
				else:
					msg="No Birthdays Today"
					break

		print(msg)
		# se=SM.SendMsg(msg,self.mobileno)
		# se.SendMessage()

		se=SWM.SendWhatsAppMsg(msg,self.mobileno)
		se.SendMessage()

	def testfunction(self):
		print(self.csv_file,self.mobileno)
