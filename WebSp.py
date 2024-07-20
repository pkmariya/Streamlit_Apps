from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as urlReq

my_url = "https://flipkart.com/search?q=iphone&otracker=start&as-show=on&as=off"
# my_url = "https://www.amazon.in/s?k=iphone+13&crid=39P6O8K2UOZHG&sprefix=iphone%2Caps%2C272&ref=nb_sb_ss_ts-doa-p_3_6"


myClient = urlReq(my_url)
page_html = myClient.read()
myClient.close()
page_soup = soup(page_html, "html.parser")

products = page_soup.findAll("div", {"class": "_4rR01T"})

prices = page_soup.findAll("div", {"class": "_30jeq3 _1_WHN1"})

ratings = page_soup.findAll("div", {"class": "_3LWZlK"})

filename = "products.csv"
f = open(filename, "w")

headers = "Product Name, Price, Rating\n"
f.write(headers)

for item in range(len(products)):
  product_name = products[item].text
  product_price = prices[item].text
  product_rating = ratings[item].text

  f.write(product_name + product_price + product_rating)
  print(product_name, product_price, product_rating)

f.close()