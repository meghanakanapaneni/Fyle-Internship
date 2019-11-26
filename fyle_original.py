#Import libraries
from PIL import Image
from PIL import ImageFile
import re
import os
ImageFile.LOAD_TRUNCATED_IMAGES = True
import pytesseract
import csv
#Function to get dates from Jul 1,2019 format(and also similar formats) to 01-07-2019 format
def get_date_4(dates_list):
	req_date=""
	for date_lists in dates_list:
		for date_strings in date_lists:
			month_str=""
			#Get integer strings
			date_string = re.findall('\d+',date_strings)
			if(len(date_string)==2):
				#Get month
				month_str=date_strings[0:3]
				#get year
				if(len(date_string[1])==2):
					year=int(date_string[1])
					if(year>=20):
						year=year+1900
					else:
						year=year+2000
				else:
					year=int(date_string[1])
				#Validate year	
				if(year>2019):
					continue
				else:	
					date_string_1=[]
					
					if(int(date_string[0])<10 and len(date_string[0])==1):
						date_string_1.append('0')
						date_string_1.append(str(date_string[0]))
						date_string_1.append('-')
					else:
						date_string_1.append(date_string[0][0])
						date_string_1.append(date_string[0][1])
						date_string_1.append('-')
					if((month_str)=='Jan' or (month_str)=='JAN' or (month_str)=='January' or (month_str)=='JANUARY'):
						date_string_1.append('0')
						date_string_1.append('1')
						date_string_1.append('-')
					elif((month_str)=='Feb' or (month_str)=='FEB' or (month_str)=='February' or (month_str)=='FEBRUARY'):
						date_string_1.append('0')
						date_string_1.append('2')
						date_string_1.append('-')
					elif((month_str)=='Mar' or (month_str)=='MAR' or (month_str)=='March' or (month_str)=='MARCH'):
						date_string_1.append('0')
						date_string_1.append('3')
						date_string_1.append('-')
					elif((month_str)=='Apr' or (month_str)=='APR' or(month_str)=='April' or (month_str)=='APRIL'):
						date_string_1.append('0')
						date_string_1.append('4')
						date_string_1.append('-')	
					elif((month_str)=='May' or (month_str)=='MAY'):
						date_string_1.append('0')
						date_string_1.append('5')
						date_string_1.append('-')
					elif((month_str)=='Jun' or (month_str)=='JUN' or (month_str)=='June' or (month_str)=='JUNE'):
						date_string_1.append('0')
						date_string_1.append('6')
						date_string_1.append('-')	
					elif((month_str)=='Jul' or (month_str)=='JUL' or (month_str)=='July' or (month_str)=='JULY'):
						date_string_1.append('0')
						date_string_1.append('7')
						date_string_1.append('-')	
					elif((month_str)=='Aug' or (month_str)=='AUG' or (month_str)=='August' or (month_str)=='AUGUST'):
						date_string_1.append('0')
						date_string_1.append('8')
						date_string_1.append('-')	
					elif((month_str)=='Sep' or (month_str)=='SEP' or (month_str)=='September' or (month_str)=='SEPTEMBER'):
						date_string_1.append('0')
						date_string_1.append('9')
						date_string_1.append('-')	
					elif((month_str)=='Oct' or (month_str)=='OCT' or (month_str)=='October' or (month_str)=='OCTOBER'):
						date_string_1.append('1')
						date_string_1.append('0')
						date_string_1.append('-')	
					elif((month_str)=='Nov' or (month_str)=='NOV' or (month_str)=='November' or (month_str)=='NOVEMBER'):
						date_string_1.append('1')
						date_string_1.append('1')
						date_string_1.append('-')
					elif((month_str)=='Dec' or (month_str)=='DEC' or (month_str)=='December' or (month_str)=='DECEMBER'):
						date_string_1.append('1')
						date_string_1.append('2')
						date_string_1.append('-')
					else:
						date_string_1.append('1')
						date_string_1.append('3')
						date_string_1.append('-')
						
				
					
					month=''.join(date_string_1[3:5])
					month=int(month)
					date=''.join(date_string_1[0:2])
					date=int(date)
					#Validate month
					if(month>31):
						req_date="None"
					#Validate date
					elif(date>31):
						req_date="None"
					
					
					else:
						req_date=""
						if(month>12):
							date_string_1[3]=date_string_1[0]
							date_string_1[4]=date_string_1[1]
							month=str(month)
							date_string_1[0]=month[0]
						#Form required date
						req_date=''.join(date_string_1)
						req_date+=str(year)
						
					
					if(req_date!="None"):
						return req_date
				
								

#Function to get dates from 12-May-2018 format to 12-05-2018 format
def get_date_3(dates_list):
	req_date=""
	for date_lists in dates_list:
		for date_string in date_lists:
			#Split the string using delimiter to get date month and year
			if '/' in date_string:
				date_string=date_string.split('/')
			
			if '-' in date_string:
				date_string=date_string.split('-')
			#Get year	
			year=int(date_string[2])
			#Validate year
			if(year>2019):
				continue
			else:	
				date_string_1=[]
				year1=list(str(date_string[2]))
				if(int(date_string[0])<10 and len(date_string[0])==1):
					date_string_1.append('0')
					date_string_1.append(str(date_string[0]))
					date_string_1.append('-')
				else:
					date_string_1.append(date_string[0][0])
					date_string_1.append(date_string[0][1])
					date_string_1.append('-')
				if((date_string[1])=='Jan' or (date_string[1])=='JAN'):
					date_string_1.append('0')
					date_string_1.append('1')
					date_string_1.append('-')
				elif((date_string[1])=='Feb' or (date_string[1])=='FEB'):
					date_string_1.append('0')
					date_string_1.append('2')
					date_string_1.append('-')
				elif((date_string[1])=='Mar' or (date_string[1])=='MAR'):
					date_string_1.append('0')
					date_string_1.append('3')
					date_string_1.append('-')
				elif((date_string[1])=='Apr' or (date_string[1])=='APR'):
					date_string_1.append('0')
					date_string_1.append('4')
					date_string_1.append('-')	
				elif((date_string[1])=='May' or (date_string[1])=='MAY'):
					date_string_1.append('0')
					date_string_1.append('5')
					date_string_1.append('-')
				elif((date_string[1])=='Jun' or (date_string[1])=='JUN'):
					date_string_1.append('0')
					date_string_1.append('6')
					date_string_1.append('-')	
				elif((date_string[1])=='Jul' or (date_string[1])=='JUL'):
					date_string_1.append('0')
					date_string_1.append('7')
					date_string_1.append('-')	
				elif((date_string[1])=='Aug' or (date_string[1])=='AUG'):
					date_string_1.append('0')
					date_string_1.append('8')
					date_string_1.append('-')	
				elif((date_string[1])=='Sep' or (date_string[1])=='SEP'):
					date_string_1.append('0')
					date_string_1.append('9')
					date_string_1.append('-')	
				elif((date_string[1])=='Oct' or (date_string[1])=='OCT'):
					date_string_1.append('1')
					date_string_1.append('0')
					date_string_1.append('-')	
				elif((date_string[1])=='Nov' or (date_string[1])=='NOV'):
					date_string_1.append('1')
					date_string_1.append('1')
					date_string_1.append('-')
				elif((date_string[1])=='Dec' or (date_string[1])=='DEC'):
					date_string_1.append('1')
					date_string_1.append('2')
					date_string_1.append('-')
				else:
					date_string_1.append('1')
					date_string_1.append('3')
					date_string_1.append('-')
					
				if(len(year1)==2):
					year=int(date_string[2])
					if(year>=20):
						year=year+1900
					else:
						year=year+2000
				
				month=''.join(date_string_1[3:5])
				month=int(month)
				date=''.join(date_string_1[0:2])
				date=int(date)
				#Validate month
				if(month>31):
					req_date="None"
				#Validate date
				elif(date>31):
					req_date="None"
				
				
				else:
					req_date=""
					if(month>12):
						date_string_1[3]=date_string_1[0]
						date_string_1[4]=date_string_1[1]
						month=str(month)
						date_string_1[0]=month[0]
					#Form required date
					req_date=''.join(date_string_1)
					req_date+=str(year)
					
				
				if(req_date!="None"):
					return req_date
								


#Function to get dates from 2000-1-1(and also similar formats) format to 01-01-2000 format
def get_date_2(dates_list):
	for date_lists in dates_list:
		for date_string in date_lists:
			#Split the string using delimiter to get date month and year
			if '/' in date_string:
				date_string=date_string.split('/')
			
			if '-' in date_string:
				date_string=date_string.split('-')
			#Get year
			year=int(date_string[0])
			#Validate year
			if(year>2019):
				continue
			else:	
				date_string_1=[]
				year1=list(date_string[0])
				date_string_1=[]
				if(int(date_string[2])<10 and len(date_string[2])==1):
					date_string_1.append('0')
					date_string_1.append(str(date_string[2]))
					date_string_1.append('-')
				else:
					date_string_1.append(str(date_string[2][0]))
					date_string_1.append(str(date_string[2][1]))
					date_string_1.append('-')
				if(int(date_string[1])<10  and len(date_string[1])==1):
					date_string_1.append('0')
					date_string_1.append(str(date_string[1]))
					date_string_1.append('-')
				else:
					date_string_1.append(str(date_string[1][0]))
					date_string_1.append(str(date_string[1][1]))
					date_string_1.append('-')
					
				if(len(year1)==2):
					year=int(date_string[0])
					if(year>=20):
						year=year+1900
					else:
						year=year+2000
				
				month=''.join(date_string_1[3:5])
				month=int(month)
				date=''.join(date_string_1[0:2])
				date=int(date)
				#Validate month
				if(month>31):
					req_date="None"
				#Validate date
				elif(date>31):
					req_date="None"
				
				
				else:
					req_date=""
					if(month>12):
						date_string_1[3]=date_string_1[0]
						date_string_1[4]=date_string_1[1]
						month=str(month)
						date_string_1[0]=month[0]
					#Form required date
					req_date=''.join(date_string_1)
					req_date+=str(year)
					
				
				if(req_date!="None"):
					return req_date
#Function to get dates from 1/2/2019 format(and also similar formats) to 01-02-2019 format					
def get_date_1(dates_list):
	req_date=""
	for date_lists in dates_list:
		for date_string in date_lists:
			#Split the string using delimiter to get date month and year
			if '/' in date_string:
				date_string=date_string.split('/')
			
			if '-' in date_string:
				date_string=date_string.split('-')
			#Get year	
			year=int(date_string[2])
			#Validate year
			if(year>2019):
				continue
			else:	
				date_string_1=[]
				year1=list(str(date_string[2]))
				if(int(date_string[0])<10 and len(date_string[0])==1):
					date_string_1.append('0')
					date_string_1.append(str(date_string[0]))
					date_string_1.append('-')
				else:
					date_string_1.append(date_string[0][0])
					date_string_1.append(date_string[0][1])
					date_string_1.append('-')
				if(int(date_string[1])<10  and len(date_string[1])==1):
					date_string_1.append('0')
					date_string_1.append(str(date_string[1]))
					date_string_1.append('-')
				else:
					date_string_1.append(date_string[1][0])
					date_string_1.append(date_string[1][1])
					date_string_1.append('-')	
				if(len(year1)==2):
					year=int(date_string[2])
					if(year>=20):
						year=year+1900
					else:
						year=year+2000
				
				month=''.join(date_string_1[3:5])
				month=int(month)
				date=''.join(date_string_1[0:2])
				date=int(date)
				#Validate month
				if(month>31):
					req_date="None"
				#Validate date
				elif(date>31):
					req_date="None"
				
				
				else:
					req_date=""
					if(month>12):
						date_string_1[3]=date_string_1[0]
						date_string_1[4]=date_string_1[1]
						month=str(month)
						date_string_1[0]=month[0]
					#Form required date
					req_date=''.join(date_string_1)
					req_date+=str(year)
					
				
				if(req_date!="None"):
					return req_date
								
				

def extract_dates(data,labels):
	#Count of correct matches
	a=0
	#Running variable for labels
	i=0
	for filename in data:
		#Declare lists to store the matches
		dates_list_1=[]
		dates_list_2=[]
		dates_list_3=[]
		dates_list_4=[]
		#get full file name
		f=foldername+filename
		text=""
		print(f)
		#Extract text from image
		text = pytesseract.image_to_string(Image.open(f)) 
		
		#finding matches of different formats of dates
		#Match 1/2/2019 format(and also similar formats)
		dates_list_1.append(re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{4}", text))
		dates_list_1.append(re.findall(r"[\d]{1,2}/[\d]{1,2}/[\d]{2}", text))
		dates_list_1.append(re.findall(r"[\d]{1,2}-[\d]{1,2}-[\d]{4}", text))
		dates_list_1.append(re.findall(r"[\d]{1,2}-[\d]{1,2}-[\d]{2}", text))
		#Match 2000-1-1(and also similar formats)
		dates_list_2.append(re.findall(r"[\d]{4}/[\d]{1,2}/[\d]{1,2}", text))
		dates_list_2.append(re.findall(r"[\d]{4}-[\d]{1,2}-[\d]{1,2}", text))
		#Match 12-May-2018 format(and also similar formats)
		dates_list_3.append(re.findall(r"[\d]{1,2}/[ADFJMNOS]\w*/[\d]{2} ", text))
		dates_list_3.append(re.findall(r"[\d]{1,2}/[ADFJMNOS]\w*/[\d]{4} ", text))
		dates_list_3.append(re.findall(r"[\d]{1,2}-[ADFJMNOS]\w*-[\d]{2} ", text))
		dates_list_3.append(re.findall(r"[\d]{1,2}-[ADFJMNOS]\w*-[\d]{4} ", text))
		#Match  Jul 1,2019 format(and also similar formats)
		dates_list_4.append(re.findall(r"[ADFJMNOS]\w*[\d]{2} .[\d]{2} ", text))
		dates_list_4.append(re.findall(r"[ADFJMNOS]\w*[\d]{2} .[\d]{4}", text))
		dates_list_4.append(re.findall(r"[ADFJMNOS]\w*[\d]{2}. [\d]{2} ", text))
		dates_list_4.append(re.findall(r"[ADFJMNOS]\w*[\d]{2}. [\d]{4}", text))
		dates_list_4.append(re.findall(r"[ADFJMNOS]\w* [\d]{2}.[\d]{2} ", text))
		dates_list_4.append(re.findall(r"[ADFJMNOS]\w* [\d]{2}.[\d]{4}", text))
		dates_list_4.append(re.findall(r"[ADFJMNOS]\w* [\d]{2}. [\d]{2} ", text))
		dates_list_4.append(re.findall(r"[ADFJMNOS]\w* [\d]{2}. [\d]{4}", text))
		dates_list_4.append(re.findall(r"[ADFJMNOS]\w* [\d]{2} .[\d]{4}", text))
		dates_list_4.append(re.findall(r"[ADFJMNOS]\w* [\d]{2} .[\d]{2} ", text))

		
		my_date=[]
		
		#Delete any empty lists
		dates_list_1 = [x for x in dates_list_1 if x]
		dates_list_2 = [x for x in dates_list_2 if x]
		dates_list_3 = [x for x in dates_list_3 if x]
		dates_list_4 = [x for x in dates_list_4 if x]
		
		#If there are any matches get the required format of date
		if(len(dates_list_1)!=0):
			my_date.append(get_date_1(dates_list_1))
		if(len(dates_list_2)!=0):
			my_date.append(get_date_2(dates_list_2))
		if(len(dates_list_3)!=0):
			my_date.append(get_date_3(dates_list_3))
		if(len(dates_list_4)!=0):
			my_date.append(get_date_4(dates_list_4))
			
		#Delete any empty lists from obtained dates	
		my_date = [x for x in my_date if x]
		#match the date with the given label
		if(len(my_date)!=0):
			#Obtained date matches the given date increase the count
			if(my_date[0]==labels[i][0]):
				a=a+1
		else:
			#Doesn't obtain any date and given None
			if(labels[i]=="None"):
				a=a+1
		i=i+1

	print("Total number of correct matches are : "+str(a))
	accuracy=(a/595)*100	
	print("Accuracy : "+str(accuracy))
    	
if __name__== "__main__":
	#Read the path
	foldername='Receipts/Receipts/'
	data = os.listdir(foldername)
	 
	# csv file name
	labels_file = "labels.csv"
	 
	# initializing the labels list
	labels = []
	 
	# reading csv file
	with open(labels_file, 'r') as csvfile:
	   	#creating a csv reader object
		csvreader = csv.reader(csvfile)
		for label in csvreader:
			labels.append(label)
	#Sort the images
	data.sort()
	#Get the date
	extract_dates(data,labels)
	
