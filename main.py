import csv
import datetime
import SendMsg as SM
import SendWhatsAppMsg as SWM

today=datetime.datetime.now().strftime("%m-%d")
today4msg=datetime.datetime.now().strftime("%B %d")
msg="*"+today4msg+" Birthdays Today:*"+'\n'+'\n'
with open('birthdays.csv',encoding="utf-8") as csvfile:
	reader=csv.DictReader(csvfile)
	for row in reader:
		if today==row['DATE']:
			msg=msg+row['NAME']+'\n'

print(msg)
# se=SM.SendMsg(msg,"+918280041455")
# se.SendMessage()

se=SWM.SendWhatsAppMsg(msg,"+918280041455")
se.SendMessage()
