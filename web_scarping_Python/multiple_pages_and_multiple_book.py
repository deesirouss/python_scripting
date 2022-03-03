import requests
import bs4

# We will do the following:

# Figure out the URL structure to go through every page
# Scrap every page in the catalogue
# Figure out what tag/class represents the Star rating
# Filter by that star rating using an if statement
# Store the results to a list
# We can see that the URL structure is the following:

# http://books.toscrape.com/catalogue/page-1.html

base_url = 'http://books.toscrape.com/catalogue/page-{}.html'

res = requests.get(base_url.format('1'))
soup = bs4.BeautifulSoup(res.text, 'lxml')
print(len(soup.select('.product_pod')))

products = soup.select(".product_pod")
# print(products[0])

# dirty-way to check 
print("star-rating Three" in str(products[0]))

# check thorugh beautiful soup
exmaple = products[0]
# print(exmaple.select('.star-rating.Three'))
print(exmaple.select('a')[1]['title'])

five_star_title = []

for n in range(1,51):
  scrape_url = base_url.format(n)
  res = requests.get(scrape_url)
  
  soup = bs4.BeautifulSoup(res.text, 'lxml')
  books = soup.select(".product_pod")
  
  for book in books:
    
    # dirty way
    # if "str-rating Two" in str(book)
    
    # other way
    if len(book.select('.star-rating.Five')) != 0:
      book_title = book.select('a')[1]['title']
      five_star_title.append(book_title)
  
print(len(five_star_title))
# first and last book in the list
print(five_star_title[0], five_star_title[-1])