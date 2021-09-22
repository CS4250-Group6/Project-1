import requests
from bs4 import BeautifulSoup

visited = set()
crawl = ['seed_url']

while len(crawl) != 0 and len(visited) < 600:

	url = crawl.pop(0)
 
 # fun(url: String) -> Bool: parse robots.txt check if the website is allowed to scrape (the url passed in will not be a robots.txt url)
	# Tasked to: Shurbur

	if url not in visited: # and allowed to scrape
  
  # fun(url: String) -> String: get page
  # Tasked to: Andrew

  # fun(page: String) -> Void: save page
  # Tasked to: Andrew

  # fun(page: String) -> list(urls: String): parse page for links
  # Tasked to: Jonathan
  
  # fun(url: String, outlinks: Int) -> Void: Saves the url and # of outlinks to a row in a file called reports.csv
  # Tasked to: Shurbur

		visited.add(url)
