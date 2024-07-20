
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as urlReq

my_url = "www.google.com"

myClient = urlReq(my_url)
page_html = myClient.read()
myClient.close()
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div", {"class": "col_2-gKeQ"})
print(len(containers))