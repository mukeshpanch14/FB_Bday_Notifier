import TodaySend as TS 
import csv
import os
import Cal2Csv as CC



# t=TS.TodaySend(csvfile,mobileno)
# #t.checkDateSend()
# t.testfunction()
files_dir='N:\\Projects\\Personal\\FB_Bday\\Files'
new_rows_list=[]

with open('controlfile.csv',encoding="utf-8") as controlfile:
	reader=csv.reader(controlfile)
	
	i=next(reader)
	new_rows_list.append(i)
	#next(reader,None)
	for row in reader:
		cal_file=os.path.join(files_dir,row[1])
		csv_file=os.path.join(files_dir,row[2])
		mobileno=row[3]
		if row[4]=='N':
			print("New Entry Generating csvfile"+row[0])
			#c=CC.Cal2Csv(os.path.join(files_dir,row[1]),os.path.join(files_dir,row[2]))
			c=CC.Cal2Csv(cal_file,csv_file)
			c.convCal2Csv()
			t=TS.TodaySend(csv_file,mobileno)
			t.testfunction()
			t.checkDateSend()
			new_row=[row[0],row[1],row[2],str(row[3]),'Y']
			new_rows_list.append(new_row)
		else:
			t=TS.TodaySend(csv_file,mobileno)
			t.testfunction()
			t.checkDateSend()
			new_rows_list.append(row)


with open('controlfile.csv','w',newline='',encoding="utf-8") as w_controlfile:
	writer=csv.writer(w_controlfile)

	writer.writerows(new_rows_list)


			