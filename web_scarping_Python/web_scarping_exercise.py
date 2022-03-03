import requests
import bs4

# TASK: Get the names of all the authors on the first page.
result = requests.get('https://quotes.toscrape.com/page/1/')
soup = bs4.BeautifulSoup(result.text, 'lxml')
# print(soup)
authors = soup.select('.author')
print(authors[0].getText())
name = []
for n in range(0,len(authors)):

  if authors[n].text not in name:
    name.append(authors[n].getText())
print(name)

# other-way could be
# authors = set() 
# for name in soup.select(".author"):
#     authors.add(name.text)

## TASK: Create a list of all the quotes on the first page.
quote = soup.select('.text')
quotes = []
for n in range(0,len(quote)):
  quotes.append(quote[n].text)
print(quotes)

# TASK: Inspect the site and use Beautiful Soup to extract the top ten tags from the requests text shown on the top right from the home page (e.g Love,Inspirational,Life, etc...). HINT: Keep in mind there are also tags underneath each quote, try to find a class only present in the top right tags, perhaps check the span.

tag_item = soup.select('.tag-item')
# print(tag_item[0])
tags = []
for tag in tag_item:
  print(tag.text)
  tags.append(tag.getText())
print(tags)

# TASK: Notice how there is more than one page, and subsequent pages look like this http://quotes.toscrape.com/page/2/. Use what you know about for loops and string concatenation to loop through all the pages and get all the unique authors on the website.
authors = set()
base_url = "https://quotes.toscrape.com/page/{}/"
for n in range(1,10):
  scrape_url = base_url.format(n)
  result = requests.get(scrape_url)
  soup = bs4.BeautifulSoup(result.text, 'lxml')
   
  for name in soup.select(".author"):
    authors.add(name.text)

print(len(authors), authors)

# to make our page number robust
# we could use something like
# if "No quotes found!" in res.text:
#   break
    