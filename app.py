"""
This script downloads and saves an image of the Deep Blue chess computer
from Wikipedia.
"""

import requests
import bs4

# imeout in secs( 10 sec)
TIMEOUT = 10

#Fetch the page content with timeout
response = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)", timeout=TIMEOUT)
soup = bs4.BeautifulSoup(response.text, 'lxml')

# Extract the image link
computer = soup.select('.mw-file-element')[1]
computer_img_link = computer['src']
full_img_url = f"https:{computer_img_link}"

# Download the image
img_data = requests.get(full_img_url,timeout=TIMEOUT).content

# Save the image
with open('my_computer_img.jpg', 'wb') as f:
    f.write(img_data)
