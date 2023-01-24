import datetime #import date, timedelta, datetime, time
import os
import time
from os import listdir
from os.path import isfile, join
import shutil

#returns list of dates between a range
def list_dates():
    dates = []
    for i in range((end_date-start_date).days + 1):
        d = start_date + datetime.timedelta(days=i)
        dates.append(datetime.datetime.strptime(str(d), '%Y-%m-%d').strftime('%Y-%#m-%d'))
    return dates
    
#Moves files between the date range to /home/ec2-user/archive/ and returns the filenames
def move_files(files, path):
    files_list = []
    dates = list_dates()
    for file in files:
        created_date = datetime.datetime.strptime(time.ctime(os.path.getctime(path + file)),"%c").strftime('%d-%#m-%Y')
        print(file, " Creation Date: ",created_date)
        if created_date in dates:
            print("Moving File")
            print(file, " Creation Date: ",created_date)
            os.replace(path + file, "/home/ec2-user/archive/%s"%file)
            files_list.append(file)
    return files_list

#Archives the /home/ec2-user/archive/ folder and stores the zip to /home/ec2-user/test-scripts/ 
def make_zip(zipname, filenames):
    # Making Zip file with current_timestamp as filename in /home/ec2-user/test-scripts/
    print("Zipping Files: ")
    shutil.make_archive("/home/ec2-user/test-scripts/%s"%zipname, 'zip', "/home/ec2-user/archive/")    

#Date range
start_date = datetime.date(2021,11, 24)  #start date
end_date = datetime.date(2021, 11, 24)  #end date

#print(list_dates())

#File Path
#A147_path = "/home/ec2-user/A147/"
cim_path = "/home/ec2-user/CIM_Export/"

#Filenames
#A147_onlyfiles = [f for f in listdir(A147_path) if isfile(join(A147_path, f))]
cim_onlyfiles = [f for f in listdir(cim_path) if isfile(join(cim_path, f))]


#list_files(A147_onlyfiles, A147_path)
cim_filenames_specific_dates = move_files(cim_onlyfiles, cim_path)
print(cim_filenames_specific_dates)
# #Will call make_zip function if there are files for specified date range.
# if cim_filenames_specific_dates:
#     cim_zip_name = "CIM-" + end_date.strftime('%Y-%#m-%d')
#     make_zip(cim_zip_name, cim_filenames_specific_dates)
