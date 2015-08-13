# Inquisitor-Python

A python redux of Kristins Spurgin's excellent Ebook-Access-Checker!
  
  -separate scripts describe each vendor
  
  -mod/edit and exisiting vendor script with your own vendor match points
  
  
  -requires:BeautifulSoup/requests
  
  -from standard library: csv/time/re
  

Instructions:

-place inquisitor.py and the vendor scripts in the same directory

-run inquisitor.py from the terminal > name your vendor [script.py] > add input .csv > add output.csv

-no headers in the .csv input file. The first column url[0] = title, the second column url[1] = url. 

-the script will write the access message to the third column of the .csv

-terminal display will count and display access messages + urls and titles for access failures
