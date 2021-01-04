from urllib.request import Request, urlopen
from requests_html import HTMLSession

session = HTMLSession()
while True:
    inp = input("Please input the item that you would like to find. Please be as specific as possible:")
    sep = "%20"
    inp = inp.split()
    inp = sep.join(inp)
    r = session.get('https://www.fairprice.com.sg/search?query=' + inp)
    links = r.html.links
    e = [x for x in links]
    for y in e:
        try:
            if y[0]+y[1]+y[2]+y[3]+y[4]+y[5]+y[6]+y[7] == "/product":
                product = y
        except:
            break
    url = Request('https://www.fairprice.com.sg' + product, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(url)

    html_bytes = page.read()
    html = html_bytes.decode("utf-8")

    nameFinder = html[html.find('\\"name\\":')+2:html.find('\\"name\\":')+30]
    nameFix = [x for x in nameFinder if x not in ["'",'"',"\\",",","}",";",")"]]
    productName = str("".join(nameFix))
    print("Is this what you were looking for? ||"+productName+"||")
    inp = input("Type yes or no:")
    if inp == "yes":
        print("Great!")
        break
    else:
        continue


"""
# FairPrice
url = Request(link, headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

priceFinder = html[html.find('\\"price\\":')+13:html.find('\\"price\\":')+20]
priceFix = [x for x in priceFinder if x not in ["'",'"',"\\",",","}",";",")"]]
price = float("".join(priceFix))
print(round(price, 2))
"""

"""
# Redmart
url = Request('https://www.lazada.sg/products/gala-apples-i301076962-s527122210.html?spm=a2o42.lazmart_search.list.1.75343f2aSWJ1G1&search=1', headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

priceFinder = html[html.find(',\"lowPrice\":')+12:html.find(',\"@type\"')]
priceFix = [x for x in priceFinder if x not in ["'",'"',"\\",",","}",";",")"]]
price = float("".join(priceFix))
print(round(price, 2))

# Giant
url = Request('https://giant.sg/unpolished-brown-rice-5kg-5021025', headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

priceFinder = html[html.find('\"price\":\"')+9:html.find('\"price\":\"')+16]
priceFix = [x for x in priceFinder if x not in ["'",'"',"\\",",","}",";",")"]]
price = float("".join(priceFix))
print(round(price, 2))

# Cold Storage
url = Request('https://coldstorage.com.sg/magnolia-5015207', headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

priceFinder = html[html.find('\"price\":\"')+9:html.find('\"price\":\"')+16]
priceFix = [x for x in priceFinder if x not in ["'",'"',"\\",",","}",";",")"]]
price = float("".join(priceFix))
print(round(price, 2))

#Eamart
url = Request('https://www.eamart.com/product/list/best-sellers/Coca-Cola-No-Sugar---Case-1032', headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

priceFinder = html[html.find('\"price\": \"')+9:html.find('\"price\": \"')+16]
priceFix = [x for x in priceFinder if x not in ["'",'"',"\\",",","}",";",")"]]
price = float("".join(priceFix))
print(round(price, 2))

#Sasha's Fine Foods
url = Request('https://sashasfinefoods.com/collections/eggs/products/nature-best-eggs', headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

priceFinder = html[html.find('\"og:price:amount\" content=\"')+27:html.find('\"og:price:amount\" content=\"')+32]
priceFix = [x for x in priceFinder if x not in ["'",'"',"\\",",","}",";",")"]]
price = float("".join(priceFix))
print(round(price, 2))

#Dei
url = Request('https://www.dei.com.sg/islandwide/retail/product/maggi-2-minute-instant-noodles-asam-laksa-5-x-78g/21845', headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

priceFinder = html[html.find('\"price\" value=\"')+15:html.find('\"price\" value=\"')+20]
priceFix = [x for x in priceFinder if x not in ["'",'"',"\\",",","}",";",")"]]
price = float("".join(priceFix))
print(round(price, 2))

#Purely Fresh
url = Request('https://www.purelyfresh.com.sg/fresh-fruits/2914-passionfruit.html', headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

priceFinder = html[html.find('price:amount\" content=\"')+23:html.find('price:amount\" content=\"')+28]
priceFix = [x for x in priceFinder if x not in ["'",'"',"\\",",","}",";",")"]]
price = float("".join(priceFix))
print(round(price, 2))

#MarketFresh.sg
url = Request('https://marketfresh.com.sg/collections/chicken/products/chicken-thigh-1pc', headers={'User-Agent': 'Mozilla/5.0'})
page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")

priceFinder = html[html.find('price:amount\" content=\"')+23:html.find('price:amount\" content=\"')+28]
priceFix = [x for x in priceFinder if x not in ["'",'"',"\\",",","}",";",")"]]
price = float("".join(priceFix))
print(round(price, 2))
"""
