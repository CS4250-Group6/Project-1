import requests
from bs4 import BeautifulSoup

def can_scrape(url):

	# The url will be a robots.txt url this time so you need to do nothing more than what's written

	# Use Andrews get_page method with the url to get the page
	# if none return true

	# Parse the page and see if we can scrape it
	# return true or false

	return True

def get_page(url):
	# requests.get(url)

	# check status code if status code is 429
	# set the program to sleep for a few seconds, idk like 3 using the time module and .sleep method

	# if the response code is greater than 299 return none

	# else return the .text of the page

	pass

def save_page(page):

	# look into how to save the page as html an file, this might be easy, or not, lmk if of any issues you face

	pass

def save_csv(url, links):

	# open a csv file called results.csv
	# write a new line to the file url(string), links(int)

	pass

def get_base_url(url):
	base_url = url

	if url[0:7] == "http://":
		base_url = base_url[7:]
	elif url[0:8] == "https://":
		base_url = base_url[8:]

	url_end = base_url.find('/')
	if url_end != -1:
		base_url = base_url[:url_end]
	return base_url

def get_links(page, baseUrl):
	links = set()
	soup = BeautifulSoup(page, "html.parser")


	for link in soup.findAll('a', href=True, download=None):
		newUrl = link.get('href')

		if newUrl[0:7] == "http://" or newUrl[0:8] == "https://":
			links.add(newUrl)
		else:
			if newUrl.find(baseUrl) == -1:
				links.add(baseUrl+newUrl)
			else:
				links.add(newUrl)

	return links




visited = set()
crawl = ['https://www.marshmellomusic.com/']

while len(crawl) != 0 and len(visited) < 600:

	url = crawl.pop(0)
	baseUrl = get_base_url(url)

	# fun(url: String) can_scrape -> Bool: parse robots.txt check if the website is allowed to scrape (more details above)
	# Tasked to: Shurbur
	if url not in visited and can_scrape(baseUrl + "/robots.txt"):

		# fun(url: String) get_page -> String: get page
		# Tasked to: Andrew
		page = get_page(url)

		if page is not None:
			# fun(page: String) -> Void: save page
			# Tasked to: Andrew
			save_page(page)
			
			# fun(page: String) -> list(urls: String): parse page for links
			# Tasked to: Jonathan
			links = get_links(page, baseUrl)

			# fun(url: String, links: Int) -> Void: save these two values in a csv file (more details above)
			save_csv(url, len(links))

		visited.add(url)
