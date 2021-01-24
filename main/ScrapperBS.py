from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
unit = str()
#url = Request('https://www.fairprice.com.sg' + product, headers={'User-Agent': 'Mozilla/5.0'})
url = Request('https://www.fairprice.com.sg/product/febreze-fabric-refresher-anti-bacterial-800ml-13029691', headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
text = soup.get_text()
priceFix = text[700:]
price = priceFix[priceFix.find("$"):priceFix.find("$")+5]   
name = text[0:text.find("|")-1]
unitFinder = soup.findAll("div", {"class": "sc-13n2dsm-10 cpkeZQ"})
unitFix = str(unitFinder)[133:]
for i in unitFix:
    if i != "<":
        unit += i 
    else: 
        break 

print(unit)