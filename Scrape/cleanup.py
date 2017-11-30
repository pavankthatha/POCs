import re
    
f = open('/tmp/POCs-master/Scrape/raw_suggestions_logs','r') 
content = f.readlines()
junk = 'b\'\\n\'\n'
initial_clean_content1 = []
initial_clean_content2 = []
initial_clean_content3 = []
initial_clean_content4 = []
initial_clean_content5 = []
initial_clean_content6 = []
initial_clean_content7 = []
initial_clean_content8 = []
clean_content = []
for line in content:
    if line != junk:
        initial_clean_content1.append(line)
for line1 in initial_clean_content1:
    initial_clean_content2.append(line1.strip('\n'))
for line2 in initial_clean_content2:
    initial_clean_content3.append(line2.strip('b'))
for line3 in initial_clean_content3:
    initial_clean_content4.append(line3.strip('\''))
for line4 in initial_clean_content4:
    initial_clean_content5.append(line4.strip('\t'))
for line5 in initial_clean_content5:
    initial_clean_content6.append(line5.strip('END'))
for line6 in initial_clean_content6:
    initial_clean_content7.append(line6.strip('START'))
for line7 in initial_clean_content7:
    initial_clean_content8.append(line7.strip(':'))


for line8 in initial_clean_content8:
    words = line8.split()
    if (len(words) > 6):
        clean_content.append(line8)
    else:
        for each in words:
            if (each[0].isdigit() and len(each)>6):
               clean_content.append(each)

for k in clean_content:
    print (k)
        




