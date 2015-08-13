#utf-8
#tested in python 2.7.10 - Daniel Sifton

from bs4 import BeautifulSoup 
import csv
import time
import re 
import requests 


#Instructions:

#place master.py and the vendor scripts in the same directory
#run master.py from the terminal > name your vendor [script.py] > add input .csv > add output.csv
#no headers in the .csv input file. The first column url[0] = title, the second column url[1] = url. 
#the script will write the access message to the third column of the .csv
#terminal display will count and display access messages + urls and titles for access failures



vendorfile = raw_input("Enter the name of vendor file . . . ")
csvfile = raw_input("Enter the name of the csv input file . . .")
csvoutfile = raw_input("Enter the name of the csv output file . . .")
urls = csv.reader(open(csvfile, "rU"))
outurls = csv.writer(open(csvoutfile, "wb"))
num_lines = len(open(csvfile).read().splitlines())
count = 1 
start_time = time.time()

execfile(vendorfile) # exec(open("./filename").read()) [mod for python 3]

print("%f seconds" % (time.time() - start_time))
