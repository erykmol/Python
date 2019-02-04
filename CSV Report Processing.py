
# coding: utf-8

# In[16]:

import csv
import pycountry as pc
import operator
import sys

def Data_converter(input_file_name,output_file_name):
    data_list=[]
    # opening file using with simultaneously takes care of the exceptions handling closing the file 
    with open(str(input_file_name), encoding='utf-8') as csv_file:
        regions_list = list(pc.subdivisions)
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            country_code = ''
            # Retrieveing 
            for i in regions_list:
                if(i.name==row[1]):
                    country_code = pc.countries.get(alpha_2 = i.country_code).alpha_3
                    break

            # Changing date format from MM/DD/YYYY to YYYY-MM-DD
            date = row[0].split('/')[::-1]
            date[1],date[2]=date[2],date[1]
            
            # Proccesing data from every row and handling ValueError
            if(country_code!=None and country_code!=''):
                row[0] = '-'.join(date)
                row[1] = country_code 
                try:
                    row[3] = str(int(int(row[2])*float(row[3].strip('%'))))
                except ValueError:
                    sys.stderr.write('Value Error with: '+row[3]+" Try checking for any trailing whitespaces")
                
            else:
                row[0] = '-'.join(date)
                row[1]='XXX'
                try:
                    row[3] = str(int(int(row[2])*float(row[3].strip('%'))))
                except ValueError:
                    sys.stderr.write('Value Error with: '+row[3]+" Try checking for any trailing whitespaces")
            data_list.append(row)
            
    # Sorting data by dates and country code, and writing it to the separate file
    sorted_data = sorted(data_list, key = operator.itemgetter(0,1))
    with open(str(output_file_name), 'w+', encoding='utf-8', newline='') as csv_out:
        csv_writer = csv.writer(csv_out, delimiter=',')
        for row in sorted_data:
            csv_writer.writerow(row)

