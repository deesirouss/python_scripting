# Task One: Grab the Google Drive Link from .csv File

import csv

data = open('find_the_link.csv',encoding="utf-8")
csv_data = csv.reader(data)
data_lines = list(csv_data)

link_list = []
for row_num,data in enumerate(data_lines):
  link_list.append(data[row_num])
link = ''.join(link_list)
print(link)

# Task Two: Download the PDF from the Google Drive link and find the phone number that is in the document.

import PyPDF2
import re

f = open('Find_the_Phone_Number.pdf','rb')
pdf = PyPDF2.PdfFileReader(f)
print(pdf.numPages)

pattern = r'\d{3}'

all_text = ''

for n in range(pdf.numPages):
    
  page = pdf.getPage(n)
  page_text = page.extractText()
  
  all_text = all_text+' '+page_text

for match in re.finditer(pattern,all_text):
  print(match)

# since 505 starting point is 41808
print(all_text[41780:41830])
# now we can see the text before phone number too

# the actual phone number pattern could be

pattern = r'\d{3}.\d{3}.\d{4}'
for match in re.finditer(pattern,all_text):
  print(match.group())
  
# for n in range(pdf.numPages):
    
#   page  = pdf.getPage(n)
#   page_text = page.extractText()
#   match = re.search(pattern,page_text)
  
#   if match:
#     print(match.group())