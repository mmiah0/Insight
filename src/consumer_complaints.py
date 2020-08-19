
import csv
from datetime import datetime
import collections
import sys

input_fname, output_fname = sys.argv[1:]
f=open('input_fname', 'r')
reader=csv.reader(f)

header = next(reader)
#data=[row for row in reader]
data=[]

for row in reader:
    # row = [Date received,Product,Sub-product,Issue,Sub-issue,Consumer complaint narrative,Company public response,Company,State,ZIP code,Tags,Consumer consent provided?,Submitted via,Date sent to company,Company response to consumer,Timely response?,Consumer disputed?,Complaint ID]
    date=datetime.strptime(row[0], '%Y-%m-%d')
    product= row[1]
    
    data.append([product, date.year]) # Append to a list the product complaints and corresponding years
    
# The lines in the output file should be sorted by product (alphabetically) and year (ascending)
data = sorted(data, key=lambda x: (x[0], x[1]))
#print data

# Add to a dictionary for products as keys and years as values
d1 = {}
for i in range(len(data)):
    d1.setdefault(data[i][0], []).append(data[i][1])
print d1

out=[]
for key,value in sorted(d1.items()):
    c = collections.Counter(value)
    #print key, value, c
    for k,v in c.items():
        print key, k, v
        out.append((key,k,v))
            
with open('output_fname','w') as f:
  writer = csv.writer(f)
  for val in out:
    f.write(str(val).strip("()")+'\n')
