#ebl
#runs via Selenium/PhantomJS [damn Javascript!]
#POST


for url in urls:

	username = ""
	password = ""

	r = requests.get(url[1], auth = (username, password))
	
	soup = BeautifulSoup(r.text)


	#browser = webdriver.PhantomJS()

	#browser.get(url[1])

	#soup=BeautifulSoup(browser.page_source)

	#browser.find_element_by_name("id").send_keys("059413")
	#browser.find_element_by_name("pin").send_keys("newhome")
	#browser.find_element_by_id("Authenticat").click()
	#time.sleep(23)
	#WebDriverWait(browser, 40).until(EC.title_is(("EBL Patron: Vancouver Island University")))
	#browser.quit() #if you want a real browser -- switch PhantomJS() to Firefox() to do this 
	

	time.sleep(25)
	if soup.find_all("div", class_="blue"):
 		print str(count) +  " of " + str(num_lines) + " | " + "Right On!" 
 		outurls.writerow([url[0], url[1], "Right On!"])
 		count += 1
	elif soup.find_all("div", class_="login-text"): 
		print str(count) +  " of " + str(num_lines) + " | " + "Nope!" + " | " + url[1] + " | " + url[0]
		outurls.writerow([url[0], url[1], "Nope!"])  
		count += 1
 	else: 
		print str(count) +  " of " + str(num_lines) + " | " + "Look into this . . . " + " | " + url[1]  + " | " + url[0]
		outurls.writerow([url[0], url[1], "Look into this . . ."])  
		count += 1
	
   













