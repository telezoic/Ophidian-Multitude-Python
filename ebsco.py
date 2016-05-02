#ebsco
#here we call Selenium/PhantomJS

for url in urls:


	browser = webdriver.PhantomJS() 

	browser.get(url[1])

	soup=BeautifulSoup(browser.page_source)
		
	if soup.find_all("a", class_= "record-type pdf-ft") or soup.find_all("a", class_= "record-type epub"):
 		print str(count) +  " of " + str(num_lines) + " | " + "Right On!" 
 		outurls.writerow([url[0], url[1], "Right On!"])
 		count += 1

 	else: 
		print str(count) +  " of " + str(num_lines) + " | " + "Nope!" + " | " + url[1]  + " | " + url[0]
		outurls.writerow([url[0], url[1], "Nope!"])  
		count += 1



