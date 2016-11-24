from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError

# F U N C T I O N S

# opens the web page and parses it
def openSite(url):
    try: 
        html = urlopen(url)
    except ValueError as e: 
        return None
    try: 
        soup = BeautifulSoup(html, 'lxml')
        text = soup.findAll(text = True) 
    except AttributeError as e: 
        return None
    return text

# receive input
website = input('Enter a URL ')

# call openSite function
text = openSite(website)

if text is None:
    print("URL could not be found")
else:
    print(text)