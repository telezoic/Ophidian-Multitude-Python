###Ophidian-Multitude-Python###

A python (2.7) redux of Kristina Spurgin's super excellent <a href="https://github.com/UNC-Libraries/Ebook-Access-Checker">Ebook-Access-Checker!</a>


![](http://www2.viu.ca/ds-dev/gitimages/multitude.png)

####What it does

Scrapes ebook/streaming video landing pages and confirms instititional access based on html source code. 

####What it doesn't . . . 

Trigger DDA autopurchases/short-term loans

####*What's different this time . . .*

1: Speed. The Ophidian-Multitude-Python runs on BeautifulSoup and Requests. Speed is much improved in the absence of a headless browser. [note: The javascript heavy Proquest/ebrary pages call for a headless browser, you may have other vendors with similar demands]

2: User interface is a trio of raw inputs, instead of a single line.

3: Separate scripts describe each vendor. Add/mod your own as needed.

4: More verbose console logging

5: Runtime benchmark
  
	
####What do you need?

	from bs4 import BeautifulSoup 

	import csv

	import time

	import re 

	import requests 
	
	from selenium import webdriver
	
BeautifulSoup, requests, and Selenium are not part of the standard Python library. So:

	pip install beautifulsoup4
	pip install requests
	pip install selenium
	
You can get PhantomJS <a href="http://phantomjs.org/">here.</a>
  
####Instructions:####

1: Create a .csv with a list of titles in the first column 	url[0] 
and urls in the second column 	url[1]. Remove your EZproxy/Authentication prefix from the urls.
Ensure there are no headers in the .csv

2: Mod/add your own vendor scripts as needed based on the apprpropriate matching syntax [from your vendor's html source code].

3: Place multitude.py and the vendor scripts in the same directory on your machine.

4: Run multitude.py from the terminal > name your vendor [vendor.py],  input.csv,  output.csv

5: The script will write the access message to the third column of the .csv

6: Terminal display will count and display access messages + urls and titles for access failures.

7: Terminal display will write out errors.

8: When the script is complete, the terminal will write out the total run time.

Note: Taylor and Francis blocked our machine IP after processing 25 URLs in < 5 min. I contacted them and told them what we we're doing and . . . wait for it . . . they have have agreed to let us process all ~19K of or T&F urls in a predefined window of time where we will not be blocked!

####Roadmap####

1: Windows testing [it's all OSX so far]

