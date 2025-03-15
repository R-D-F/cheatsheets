# BeautifulSoup (bs4) Cheat Sheet

# 1. Install dependencies
# pip install beautifulsoup4 lxml

from bs4 import BeautifulSoup

# 2. Create a BeautifulSoup object
html = "<html><body><h1>Hello</h1></body></html>"
soup = BeautifulSoup(html, "lxml")  # or "html.parser"

# 3. Basic Navigation
print(soup.title)  # Gets <title> tag
print(soup.title.string)  # Gets title text
print(soup.body)  # Gets <body> tag
print(soup.h1)  # Gets first <h1> tag

# 4. Searching the DOM
# 4.1 Find one element
print(soup.find("h1"))  # Returns first <h1>
print(soup.find("div", class_="content"))  # Find by class
print(soup.find("a", {"href": "#link"}))  # Find by attribute

# 4.2 Find all elements
print(soup.find_all("p"))  # All <p> tags
print(soup.find_all(["h1", "h2", "h3"]))  # Multiple tags
print(soup.find_all("div", limit=3))  # Limit results

# 5. CSS Selectors
print(soup.select("div.content"))  # Selects div with class="content"
print(soup.select("#main"))  # Selects element with id="main"
print(soup.select("div > p"))  # Direct child <p> inside <div>
print(soup.select("a[href*='example']"))  # Selects links with "example" in href

# 6. Extracting Data
tag = soup.find("a")
if tag:
    print(tag.name)  # 'a'
    print(tag.attrs)  # {'href': 'https://example.com'}
    print(tag["href"])  # 'https://example.com'
    print(tag.get("href"))  # Same as above

# 7. Modifying Elements
h1_tag = soup.find("h1")
if h1_tag:
    h1_tag.string = "New Title"

p_tag = soup.find("p")
if p_tag:
    p_tag["class"] = "new-class"

# 8. Adding & Removing Elements
new_tag = soup.new_tag("span", style="color:red")
new_tag.string = "Important"
soup.body.append(new_tag)  # Adds to <body>

p_tag = soup.find("p")
if p_tag:
    p_tag.decompose()  # Completely removes a tag

# 9. Navigating the DOM
print(soup.head.next_element)  # Next element inside <head>
print(soup.body.previous_element)  # Previous element
print(soup.h1.parent)  # Gets parent of <h1>
print(soup.h1.find_next_sibling())  # Next sibling
print(soup.h1.find_previous_sibling())  # Previous sibling

# 10. Extracting Text
print(soup.get_text())  # Gets all text from page
p_tag = soup.find("p")
if p_tag:
    print(p_tag.get_text(strip=True))  # Text from <p>, no spaces

# 11. Handling Encodings
soup = BeautifulSoup(html, "lxml", from_encoding="utf-8")

# Print final parsed HTML
print(soup.prettify())
