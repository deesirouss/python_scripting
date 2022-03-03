import requests
import bs4

# grabing title of this website

result = requests.get("https://en.wikipedia.org/wiki/Jonas_Salk")

print(type(result))
# print(result.text)

soup = bs4.BeautifulSoup(result.text, "lxml")
# print(soup)
print(soup.select('title'))
print(len(soup.select('p')))
print(soup.select('title')[0].getText())


# Syntax to pass to the .select() method

# Match Results

# soup.select('div')

# All elements with the <div> tag

# soup.select('#some_id')

# The HTML element containing the id attribute of some_id

# soup.select('.notice')

# All the HTML elements with the CSS class named notice

# soup.select('div span')

# Any elements named <span> that are within an element named <div>

# soup.select('div > span')

# Any elements named <span> that are directly within an element named <div>, with no other element in between

## grabing contents table string from above site

# print(soup.select('.toctext'))
contents = soup.select('.toctext')
print(contents[0].text)

for item in soup.select('.toctext'):
  print(item.text)
  

# grabing images form website

images = soup.select('.image')[0]

# image1 = images[0]
print(images)
image_link = requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/5/59/Jonas_Salk_candid.jpg/220px-Jonas_Salk_candid.jpg")
f = open('/home/bibek/git/python_scripting/web_scarping_Python/Jonas_Salk.jpg','wb')
f.write(image_link.content)
f.close()