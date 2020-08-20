#!/bin/bash
import csv
from datetime import datetime
import collections
import sys

input_fname, output_fname = sys.argv[1:]
f=open(input_fname, 'r')
reader=csv.reader(f)

header = next(reader)
#data=[row for row in reader]
data=[]

for row in reader:
    # row = [Date received,Product,Sub-product,Issue,Sub-issue,Consumer complaint narrative,Company public response,Company,State,ZIP code,Tags,Consumer consent provided?,Submitted via,Date sent to company,Company response to consumer,Timely response?,Consumer disputed?,Complaint ID]
    date=int(datetime.strptime(row[0], '%Y-%m-%d').year)
    product= row[1]
    
    data.append([product, date]) # Append to a list only the year from datetime with product complaints
    
# The lines in the output file should be sorted by product (alphabetically) and year (ascending)
#data = sorted(data, key=lambda x: (x[0], x[1]))
#print data

d1 = {}
for i in range(len(data)):
    d1.setdefault(data[i][0], []).append(data[i][1])
print d1

out=[]
for key,value in sorted(d1.items(), key=lambda x: x[0]):
    c = collections.Counter(value)
    #print key, value, c
    for k,v in sorted(c.items(), key=lambda x: x[0]):
        print key, k, v
        out.append((key,k,v))
            
with open(output_fname,'w') as f:
  writer = csv.writer(f)
  for val in out:
    f.write(str(val).strip("()")+'\n')
# Sample output

#'Product, year, tot_compl_received, atleast_one_compl, %_comp_filed\n'    
#"credit reporting, credit repair services, or other personal consumer reports",2019,3,2,67
#"credit reporting, credit repair services, or other personal consumer reports",2020,1,1,100
#debt collection,2019,1,1,100
