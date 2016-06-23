import scrapy
import string
'''import re'''


#to stop program hit ctrl+c two times
from tutorial.items import rateyourmusicartist # here I have imported the artist item, it contains name, dob and nationality
#global artistcounter



class DmozSpider(scrapy.Spider):
	'''
	invalidChars = set(string.punctuation.replace("_", ""))
	if any(char in invalidChars for char in word):
	print "Invalid"
	else:
	print "Valid"
	'''
	
	#def special_match(strg, search=re.compile(r'[^a-z0-9.]').search):
	#	return not bool(search(strg))
		#special_match("az09.#")
	
	print 'HELLOOOOOO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
	name = "dmoz2"
	allowed_domains = ["rateyourmusic.com"]
	start_urls = [
		#"http://www.rateyourmusic.com/customchart?page=1&chart_type=top&type=album&year=2010s&genre_include=1&include_child_genres=1&genres=&include_child_genres_chk=1&include=both&origin_countries=&limit=none&countries= ",
		#"http://rateyourmusic.com/customchart?page=2&chart_type=top&type=album&year=2010s&genre_include=1&include_child_genres=1&genres=&include_child_genres_chk=1&include=both&origin_countries=&limit=none&countries=",
		#"http://rateyourmusic.com/customchart?page=3&chart_type=top&type=album&year=2010s&genre_include=1&include_child_genres=1&genres=&include_child_genres_chk=1&include=both&origin_countries=&limit=none&countries=",
		#"http://rateyourmusic.com/customchart?page=4&chart_type=top&type=album&year=2010s&genre_include=1&include_child_genres=1&genres=&include_child_genres_chk=1&include=both&origin_countries=&limit=none&countries=",
		#"http://rateyourmusic.com/customchart?page=5&chart_type=top&type=album&year=2010s&genre_include=1&include_child_genres=1&genres=&include_child_genres_chk=1&include=both&origin_countries=&limit=none&countries=",
		#"http://rateyourmusic.com/customchart?page=6&chart_type=top&type=album&year=2010s&genre_include=1&include_child_genres=1&genres=&include_child_genres_chk=1&include=both&origin_countries=&limit=none&countries=",
		#"http://rateyourmusic.com/customchart?page=7&chart_type=top&type=album&year=2010s&genre_include=1&include_child_genres=1&genres=&include_child_genres_chk=1&include=both&origin_countries=&limit=none&countries=",
		#"http://rateyourmusic.com/customchart?page=8&chart_type=top&type=album&year=2010s&genre_include=1&include_child_genres=1&genres=&include_child_genres_chk=1&include=both&origin_countries=&limit=none&countries=",
		#"http://rateyourmusic.com/customchart?page=9&chart_type=top&type=album&year=2010s&genre_include=1&include_child_genres=1&genres=&include_child_genres_chk=1&include=both&origin_countries=&limit=none&countries=",
		"http://rateyourmusic.com/customchart?page=10&chart_type=top&type=album&year=2010s&genre_include=1&include_child_genres=1&genres=&include_child_genres_chk=1&include=both&origin_countries=&limit=none&countries="
	]

	def parse(self, response):
		artistcounter = 0
		for href in response.xpath('//table[@class="mbgen"]/tr/td[3]/div/span/a/@href'):
			link = href.extract()
			url = 'http://www.rateyourmusic.com'+link
			
			'''
			#checking url is artist page
			if link[:7] == ('/artist'): #this code is handy to check if a string contains weird characters, make sure to import re
				#item['name'] = link[8:] #I want to place this in the parse_dir_contents method
				#if re.match("^[A-Za-z0-9_-]*$", link[8:]):
				#	print 'artist found :' + link[8:] 
				#else :
				#	print 'artist found :Invalid Chars!!!!!!!!!!!!!!!!'
					
				yield scrapy.Request(url, callback=self.parse_dir_contents)
				#yield item
			'''
			
			#checking url is artist page
			if link[:7] == ('/artist'):
				yield scrapy.Request(url, callback=self.parse_dir_contents)
				
			
			#checking url is album page, I want to ignore this for the moment
			#if link[:14] == ('/release/album'):
				#yield scrapy.Request(url, callback=self.parse_dir_contents2)
				
	def parse_dir_contents(self, response): #this works
		print 'Found Artist !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
		item = rateyourmusicartist()
		
		for sel in response.xpath('//table[@class="artist_info"]/tr[1]/td'): 
			#if () == ():
			item['dateofbirth'] = sel.xpath('text()').extract()
			item['nationality'] = sel.xpath('a/text()').extract()
		
		for sel in response.xpath('//table[@class="artist_info"]/tr[2]/td'): #//*[@id="content"]/div[4]/div[1]/div[1]/div[2]/table/tbody/tr[2]/td/a
			item['status'] = sel.xpath('div/text()').extract()
			#item['statusinfo'] = sel.xpath('a/text()').extract()
			
			#if sel.xpath('div/text()').extract() == ('Currently'):
				#item['currently'] = sel.xpath('a/text()').extract()
		
		item['statusinfo'] = ", ".join(response.xpath('//table[@class="artist_info"]/tr[2]/td/a/text()').extract())
		
		item['statusinfo2'] = ", ".join(response.xpath('//table[@class="artist_info"]/tr[2]/td/text()').extract())
			
		#genres = ''
		
		item['genre'] = ", ".join(response.xpath('//a[@class="genre"]/text()').extract())
		
		#//*[@id="content"]/div[4]/div[1]/div[1]/div[2]/table/tbody/tr[2]/td/div
		#item['artisttype'] = response.xpath('//div[@class="info_hdr"]/text()').extract()
		
		#//*[@id="content"]/div[4]/div[1]/div[1]/div[2]/table/tbody/tr[1]/td/div
		#for sel in response.xpath('//div/div/div/div/table/tbody/tr[2]/td/div[@class="info_hdr"]'): 
		
		for sel in response.xpath('//table[@class="artist_info"]/tr[1]/td/div'): 
			item['artisttype'] = sel.xpath('text()').extract()
		
		#for sel in response.xpath('//a[@class="genre"]'):     #title[@lang='en']
			#item['genre'] = sel.xpath('text()').extract()
			#genres = genres + sel.xpath('text()').extract() + ', '
			#item['genre'] = ", ".join(sel.xpath('text()').extract())
		
		#item['genre'] = genres
		
		for sel in response.xpath('//div/div/div/div/div/h1'): 
			item['name'] = sel.xpath('text()').extract()
		
		yield item
	
	'''
	def parse_dir_contents2(self, response): #this doesen't work yet
		print 'Found Album !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
		item = rateyourmusicalbum()
		
		for sel in response.xpath('//table[@class="album_info"]/tbody/tr/td[1]/table/tbody'): #this first line should contain the xpath of a single item 
			releasedate = sel.xpath('tr[3]/td/text()').extract() + " " + sel.xpath('tr[3]/td/a/b/text()').extract()
			#item['date'] = sel.xpath('text()').extract() #/tr[3]/td/text() #date
														#/tr[3]/td/a/b/text() #year
			item['date'] = releasedate
			item['rating'] = sel.xpath('tr[5]/td/span/span[1]/text()').extract() #/tr[5]/td/span/span[1]/text()
			item['artist'] = sel.xpath('tr[1]/td/span[1]/a/text()').extract() #/tr[1]/td/span[1]/a/text()
			
		for sel in response.xpath('//html/head/title'): #this first line should contain the xpath of a single item
			#/html/head/title
			item['title'] = sel.xpath('text()').extract() #from here you grab items within this xpath such as text or data
			
		yield item
		
	'''	
		
		
		
		
		
		
		#print 'HELLOOOOOO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!'
		#to save as a CSV just run scrapy crawl dmoz2 -0 text.csv