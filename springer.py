#springer


 


for url in urls:


	r = requests.get(url[1])

	soup = BeautifulSoup(r.text)

	if soup.find_all("a", class_= "webtrekk-track pdf-link"): 
 		print str(count) +  " of " + str(num_lines) + " | " + "Right On!" 
 		outurls.writerow([url[0], url[1], "Right On!"])
 		count += 1
	elif soup.find_all("a", class_= "access-link"):
		print str(count) +  " of " + str(num_lines) + " | " + "Nope!" + " | " + url[1] + " | " + url[0]
		outurls.writerow([url[0], url[1], "Nope!"])  
		count += 1
	elif soup.find_all("title", text = re.compile("Deleted DOI")):
		print str(count) +  " of " + str(num_lines) + " | " + "Deleted DOI!" + " | " + url[1] + " | " + url[0]
		outurls.writerow([url[0], url[1], "Deleted DOI!"]) 
		count += 1	
	elif soup.find_all("div", id = "error"):
		print str(count) +  " of " + str(num_lines) + " | " + "Page not found!" + " | " + url[1] + " | " + url[0]
		outurls.writerow([url[0], url[1], "Page not Found!"])  
		count += 1 
 	else: 
		print str(count) +  " of " + str(num_lines) + " | " + "Look into this . . . " + " | " + url[1]  + " | " + url[0]
		outurls.writerow([url[0], url[1], "Look into this . . ."])  
		count += 1


