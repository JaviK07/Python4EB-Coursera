import urllib.request
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the span tags
tags = soup.find_all('span')
sum = 0
for tag in tags:
    # Extract the number from the contents of the span tag
    number = int(tag.contents[0])
    sum += number

# Print the sum of the values
print("Sum of values within <span> tags:", sum)