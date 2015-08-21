### Inquisitor-Python###

A python (2.7) redux of Kristins Spurgin's super excellent <a href="https://github.com/UNC-Libraries/Ebook-Access-Checker">Ebook-Access-Checker!</a>

*What's different this time . . .*

1: Speed. The Inquisitor-Python runs on BeautifulSoup and Requests. Speed is much improved in the absence of a headless browser.

2: User interface is a trio of raw inputs, instead of a single line.

3: Separate scripts describe each vendor. Add/mod your own as needed.

4: More verbose console logging

5: Benchmark runtime
  
	
####What do you need?

	from bs4 import BeautifulSoup 

	import csv

	import time

	import re 

	import requests 
	
BeautifulSoup and requests are not part of the standard Python library. So:

	pip install beautifulsoup4
	pip install requests
  
####Instructions:####

1: Create a .csv with a list of titles in the first column 	url[0] 
and urls in the second column 	url[1] 
Ensure there are no headers in the .csv

2: Mod/add your own vendor scripts as needed based on the apprpropriate matching syntax [from your vendor's html source code].

3: Place inquisitor.py and the vendor scripts in the same directory on your machine.

2: Run inquisitor.py from the terminal > name your vendor [vendor.py],  input.csv,  output.csv

4: The script will write the access message to the third column of the .csv

5: Terminal display will count and display access messages + urls and titles for access failures.

6: Terminal display will write out errors.

7: When the script is complete, the terminal will write out the total run time.

####Roadmap####

1: Windows testing [it's all OSX so far]

