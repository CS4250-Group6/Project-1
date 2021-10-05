import requests
import time
import csv
import urllib.request
from langdetect import detect
from bs4 import BeautifulSoup


def can_scrape(robots, url):
    print(url)
    merged_url = (url + '/robots.txt')
    open_page = get_page(robots)
    if open_page is not None:
        split_by_line = open_page.split('\n')
        # print(url)

        # print(split_by_line)
        for each_line in split_by_line:
            # print(each_line)
            if ':' in each_line:
                pre_colon = each_line.split(":")
                print(merged_url)
                beginning = merged_url.split('/')
                # print("pre_colon:",pre_colon[1])
                print(pre_colon[1])
                print('beginning:', beginning[1])
                if beginning[1] == pre_colon[1]:
                    print("WORKED")
                    print(url)
                    # print(each_line[0])

                    # print(pre_colon)
                    if pre_colon[0] == "Disallow":

                        continue


                    elif pre_colon[0] == "Allow":
                        return True
                else:
                    return True
            else:
                continue
    else:
        return True


# The url will be a robots.txt url this time so you need to do nothing more than what's written

# Use Andrews get_page method with the url to get the page
# if none return true, else...

# Parse the robots.txt page and see if we can scrape it
# return true or false


def get_page(url):
    site = requests.get("http://" + url)

    if site.status_code == 429:
        time.sleep(3)
        return get_page(url)
    elif site.status_code < 300:
        return site.text
    else:
        return None


def save_page(page, file_name):
    # Saving and extracting into file, probably
    with open(file_name, 'w') as f:
        f.write(page)
        f.close()


# urllib.request.urlretrieve('https://www.marshmellomusic.com/', 'page.html') # using urllib library as an alternative

def save_csv(url, links):

    with open('Project_1_results.csv', 'a') as file:
        writer = csv.writer(file)
        row = url, links
        writer.writerow(row)


def replace_http_protocol(url):
    new_url = url

    if url[0:7] == "http://":
        new_url = new_url[7:]
    elif url[0:8] == "https://":
        new_url = new_url[8:]

    return new_url


def get_base_url(url):
    base_url = replace_http_protocol(url)

    url_end = base_url.find('/')
    if url_end != -1:
        base_url = base_url[:url_end]
    return base_url


def get_links(soup, baseUrl):
    links = set()

    for link in soup.findAll('a', href=True, download=None):
        newUrl = link.get('href')
        if newUrl is not None:
            if newUrl[0:7] == "http://" or newUrl[0:8] == "https://":
                links.add(replace_http_protocol(url))
            elif not newUrl.startswith('#') and not newUrl.startswith('ftp://') and not newUrl.startswith('mailto:'):
                if newUrl.find(baseUrl) == -1:
                    links.add(baseUrl + newUrl)
                else:
                    links.add(newUrl)

    return links


visited = set()
crawl = ['www.en.wikipedia.org/wiki/Web_crawler']

while len(crawl) != 0 and len(visited) < 600:

    url = crawl.pop(0)
    baseUrl = get_base_url(url)

    # fun(url: String) can_scrape -> Bool: parse robots.txt check if the website is allowed to scrape (more details above)
    # Tasked to: Shurbur
    if url not in visited and can_scrape(baseUrl + "/robots.txt", url)==True:

        # fun(url: String) get_page -> String: get page
        # Tasked to: Andrew
        page = get_page(url)

        if page is not None:

            soup = BeautifulSoup(page, "html.parser")
            print("here")
            if detect(soup.get_text()) == 'en':
                # fun(page: String, file_name: String) -> Void: save page
                # Tasked to: Andrew
                save_page(page, "page{}.html".format(len(visited) + 1))

                # fun(page: String) -> list(urls: String): parse page for links
                # Tasked to: Jonathan
                links = get_links(soup, baseUrl)

                # fun(url: String, links: Int) -> Void: save these two values in a csv file (more details above)
                save_csv(url, len(links))

                crawl += list(links)
                time.sleep(.5)

        visited.add(url)
