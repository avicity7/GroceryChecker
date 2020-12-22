from urllib.request import Request, urlopen

# FairPrice
url = Request('https://www.fairprice.com.sg/product/13111689', headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

priceFinder = html[html.find('\\"price\\":')+13:html.find('\\"price\\":')+20]
priceFix = [x for x in priceFinder if x not in ["'",'"',"\\",","]]
price = float("".join(priceFix))
print(round(price, 2))

# Redmart
url = Request('https://www.lazada.sg/products/gala-apples-i301076962-s527122210.html?spm=a2o42.lazmart_search.list.1.75343f2aSWJ1G1&search=1', headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

priceFinder = html[html.find(',\"lowPrice\":')+12:html.find(',\"@type\"')]
priceFix = [x for x in priceFinder if x not in ["'", '"', "\\", ","]]
price = float("".join(priceFix))
print(round(price, 2))



    

