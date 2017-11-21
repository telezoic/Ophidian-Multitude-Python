#adam [adam matthew digital]



for url in urls:


	r = requests.get(url[1])

	soup = BeautifulSoup(r.text, "lxml")
		
	if soup.find_all(text = re.compile("Download whole document")) or soup.find_all(text = re.compile("Download entire document")):
 		print str(count) +  " of " + str(num_lines) + " | " + "Right On!" 
 		outurls.writerow([url[0], url[1], "Right On!"])
 		count += 1
 	else: 
		print str(count) +  " of " + str(num_lines) + " | " + "Look into this . . . " + " | " + url[1]  + " | " + url[0]
		outurls.writerow([url[0], url[1], "Look into this . . ."])  
		count += 1
