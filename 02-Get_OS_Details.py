#!/usr/bin/python3

import os
import csv
import json

from datetime import *
date = date.today()
time = datetime.now()
file_path = time.strftime("Daily_Reports_%Y-%m-%d_%H-%M.csv")

json_file="01-Linux_Command.json"
with open(json_file) as jf:
    my_dict = json.load(jf)

os_name=os.popen(my_dict['os_flavour']).read().strip('\n')
print(os_name)

if os_name == 'ubuntu':
    print("**** UBUNTU OS found and we are collecting information , Please wait!!!! ****")

    # Hostname details
    hostname = os.popen(my_dict['hostname']).read().strip('\n')

    # IP details
    ip = os.popen(my_dict['ip_address']).read().strip('\n')

    # File System details
    df_details = os.popen(my_dict['df_details']).read().strip('\n')


    # Data csv
    data_csv = [hostname, ip,df_details]
    print(data_csv)

    # Storing variable into list for inserting CSV data
    header_csv = (my_dict['header_para'])
    print(header_csv)

    # Saving Linux data into a csv file
    file = open(file_path, 'a+')
    writer = csv.writer(file)
    writer.writerow(header_csv)
    writer.writerow(data_csv)
    file.close()
    print("File Import SUCCESSFULLY from your Current Directory" +file_path)
