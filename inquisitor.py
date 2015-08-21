#utf-8
#tested in python 2.7.10 - Daniel Sifton

from bs4 import BeautifulSoup 
import csv
import time
import re 
import requests 

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
