from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
unit = str()
temp = int()
#url = Request('https://www.fairprice.com.sg' + product, headers={'User-Agent': 'Mozilla/5.0'})
url = Request('https://www.fairprice.com.sg/product/canard-duchene-charles-vii-blanc-de-blancs-6-x-750ml-90050191', headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
text = soup.get_text()
priceFix = text[700:]
price = priceFix[priceFix.find("$"):priceFix.find("$")+10]
for i in range(5,10):
    try: 
        temp = int(price[i])
    except: 
        price = price[0:i]
name = text[0:text.find("|")-1]
unitFinder = soup.findAll("div", {"class": "sc-13n2dsm-10 cpkeZQ"})
unitFix = str(unitFinder)[133:]
for i in unitFix:
    if i not in ["<", '"', "'", "!", "/"]:
        unit += i 
    else: 
        break 
print(price)
