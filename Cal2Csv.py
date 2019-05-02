from icalendar import Calendar,Event
import datetime
import csv

class Cal2Csv(object):
	def __init__(self,cal_file,bday_csv):
		self.cal_file=cal_file
		self.bday_csv=bday_csv

	def convCal2Csv(self):	
		g=open(self.cal_file,'rb')
		gcal=Calendar.from_ical(g.read())
		with open(self.bday_csv,'w',newline='',encoding="utf-8") as csvfile:
			writer=csv.writer(csvfile)
			writer.writerow(['DATE','NAME','UID'])
			for component in gcal.walk():
				if component.name=="VEVENT":
					summ=component.get('summary')
					name=str(summ).split("'",1)
					dt_comp=component.get('dtstart')
					str_dt=dt_comp.dt.strftime("%m-%d")
					str_uid=str(component.get('uid'))
					writer.writerow([str_dt,name[0],str_uid])

		g.close()