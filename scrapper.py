from urllib.request import Request, urlopen

url = Request('https://www.fairprice.com.sg/product/13111689', headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

priceFinder = html[html.find('\\"price\\":')+13:html.find('\\"price\\":')+20]
priceFix = [x for x in priceFinder if x not in ["'",'"',"\\",","]]
price = float("".join(priceFix))
print(round(price, 2))


    

