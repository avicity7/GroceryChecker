from urllib.request import Request, urlopen
from requests_html import HTMLSession
from bs4 import BeautifulSoup

# Price Comparison
# Storage structure:
# item_price = ["item_1",[price1, price2, price3],"item_2",[price1, price2, price3]]
# item_name = ["item_1",[name1, name2, name3],"item_2",[name1, name2, name3]]
# item_qty = ["item_1",[qty1, qty2, qty3],"item_2",[qty1, qty2, qty3]]
item_price = []
item_name = []
item_qty = []
store_name = []
final = []

def addItem(item):
    item_price.append(item)
    item_name.append(item)
    item_qty.append(item)
    store_name.append(item)
    
def addPrices(price, name, qty, store, item_no):
    item_price[item_no].append(price)
    item_name[item_no].append(name)
    item_qty[item_no].append(qty)
    store_name[item_no].append(store)

def finalAddItem(price, name, qty, store):
    final.append([price, name, qty, store])

def priceComparison():
    for item in item_price:
        lowest = 10000000
        for price in item:
            if price < lowest:
                lowest = price
        y = item_price.index(item)
        x = item.index(lowest)
        finalAddItem(item[x], item_name[y][x], item_qty[y][x], store_name[y][x])

def storeSearch(searchString):
    #Cold Storage Search
    lst = [] 
    temp = 0
    sep = "+"
    coldSearch = searchString.split()
    coldSearch = sep.join(coldSearch)
    url = Request('https://coldstorage.com.sg/search?q=' + coldSearch, headers={'User-Agent': 'Mozilla/5.0'})
    page = urlopen(url)
    #Getting item parameters
    productUnit = ""
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text()
    unitFinder = soup.findAll("div", {"class": "content_price"})
    first, second,third = int(),int(),int()
    decimal = str()

    for i in range(0,len(str(unitFinder[0]))):
        try: 
            first = int(str(unitFinder[0])[i])
            decimal = str(unitFinder[0])[i+1]
            second = int(str(unitFinder[0])[i+2])
            third = int(str(unitFinder[0])[i+3])
            break
        except: 
            continue

    price = str(first) + decimal + str(second) + str(third)
    #DEI HURRY LA
    product = str()
    session = HTMLSession()
    r = session.get('https://www.dei.com.sg/search?_token=aRkpJ3nCKN5iArm0CpLMEz0gBtxPYF5DyPrk36T6&search=fisherman+friend')
    links = r.html.links
    e = [x for x in links]
    for y in e:
        try:
            if y[40]+y[41]+y[42]+y[43]+y[44]+y[45]+y[46]+y[47] == "/product":
                product = y
                break
        except:
            continue
    return price

extraLinks = []
session = HTMLSession()
productUnit = ""
while True:
    inp = input("Please input the item that you would like to find. Please be as specific as possible:")
    sep = "%20"
    inp = inp.split()
    inp = sep.join(inp)
    try:
        #Getting links from Fairprice search page 
        r = session.get('https://www.fairprice.com.sg/search?query=' + inp)
        links = r.html.links
        e = [x for x in links]
        for y in e:
            try:
                if y[0]+y[1]+y[2]+y[3]+y[4]+y[5]+y[6]+y[7] == "/product":
                    product = y
                    break
            except:
                continue
        url = Request('https://www.fairprice.com.sg' + product, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(url)
        #Getting item parameters
        productUnit = ""
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text()
        priceFix = text[700:]
        price = priceFix[priceFix.find("$"):priceFix.find("$")+10]
        for i in range(5,10):
            try: 
                temp = int(price[i])
            except: 
                price = price[0:i]
        productName = text[0:text.find("|")-1]
        unitFinder = soup.findAll("div", {"class": "sc-13n2dsm-10 cpkeZQ"})
        unitFix = str(unitFinder)[133:]
        for i in unitFix:
            if i != "<":
                productUnit += i 
            else: 
                break 
        
        print("\nItem found: {productname} {productunit} {cost}".format(productname = productName, productunit = productUnit, cost = price))
        print("\nIs this the item that you were looking for?")
        inp = input("\nType yes or no:")
        #When item found is correct: 
        if inp == "yes":
            search = productName +" " + productUnit
            print(storeSearch(search))
            break
        #When item found is incorrect, going through other search results in Fairprice search: 
        elif inp == "no":
            print("\nAlright! We'll display the other top 5 search results:")
            for times in range (1,6):
                e.remove(product)
                for y in e:
                    try:
                        if y[0]+y[1]+y[2]+y[3]+y[4]+y[5]+y[6]+y[7] == "/product":
                            product = y
                            url = Request('https://www.fairprice.com.sg' + product, headers={'User-Agent': 'Mozilla/5.0'})
                            page = urlopen(url)
                            productUnit = ""
                            html_bytes = page.read()
                            html = html_bytes.decode("utf-8")
                            soup = BeautifulSoup(html, "html.parser")
                            text = soup.get_text()
                            priceFix = text[700:]
                            price = priceFix[priceFix.find("$"):priceFix.find("$")+10]
                            for i in range(5,10):
                                try: 
                                    temp = int(price[i])
                                except: 
                                    price = price[0:i]
                            productName = text[0:text.find("|")-1]
                            unitFinder = soup.findAll("div", {"class": "sc-13n2dsm-10 cpkeZQ"})
                            unitFix = str(unitFinder)[133:]
                            for i in unitFix:
                                if i != "<":
                                    productUnit += i 
                                else: 
                                    break 

                            extraLinks.append(product)        
                            print("{time}. {productname} {productunit} {cost}".format(time = times, productname = productName, productunit = productUnit, cost = price))
                            break
                    except:
                        continue

            inp = input("\nWhich of these are what you are looking for? Enter 0 if it is none of them, else enter the number of the item:")
            if inp == "0":
                continue
            #Correct item found 
            else:
                url = Request('https://www.fairprice.com.sg' + extraLinks[int(inp)-1], headers={'User-Agent': 'Mozilla/5.0'})
                page = urlopen(url)
                productUnit = ""
                html_bytes = page.read()
                html = html_bytes.decode("utf-8")
                soup = BeautifulSoup(html, "html.parser")
                text = soup.get_text()
                priceFix = text[700:]
                price = priceFix[priceFix.find("$"):priceFix.find("$")+10]
                for i in range(5,10):
                    try: 
                        temp = int(price[i])
                    except: 
                        price = price[0:i]
                productName = text[0:text.find("|")-1]
                unitFinder = soup.findAll("div", {"class": "sc-13n2dsm-10 cpkeZQ"})
                unitFix = str(unitFinder)[133:]
                for i in unitFix:
                    if i != "<":
                        productUnit += i 
                    else: 
                        break
                search = productName +" " + productUnit
                print(storeSearch(search))
                break
                          
    except:
        print("\nSorry, we are not able to find that item. Please enter a different item or name.")
        continue



'''
# FairPrice
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
'''

'''
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
soup = BeautifulSoup(html, "html.parser")
text = soup.get_text()
priceFix = text[8400:]
price = priceFix[priceFix.find("$"):priceFix.find("$")+10]
for i in range(5,10):
    try: 
        temp = int(price[i])
    except: 
        price = price[0:i]
name = text[0:text.find("|")-1]
unitFinder = soup.findAll("div", {"class": "product_size product_detail"})
unitFix = str(unitFinder)[69:]
for i in unitFix:
    if i not in ["<", '"', "'", "!", "/"]:
        unit += i 
    else: 
        break
# Cold Storage
soup = BeautifulSoup(html, "html.parser")
text = soup.get_text()
priceFix = text[8500:]
price = priceFix[priceFix.find("$"):priceFix.find("$")+10]
for i in range(5,10):
    try: 
        temp = int(price[i])
    except: 
        price = price[0:i]
name = text[0:text.find("|")-1]
unitFinder = soup.findAll("div", {"class": "product_size product_detail"})
unitFix = str(unitFinder)[69:]
for i in unitFix:
    if i not in ["<", '"', "'", "!", "/"]:
        unit += i 
    else: 
        break 
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
soup = BeautifulSoup(html, "html.parser")
text = soup.get_text()
priceFix = text[2700:]
price = priceFix[priceFix.find("$"):priceFix.find("$")+10]
for i in range(5,10):
    try: 
        temp = int(price[i])
    except: 
        price = price[0:i]
name = text[9:text.find("|")-1]
nom = name.split(" - ")
weight = nom[-1]
#Purely Fresh
soup = BeautifulSoup(html, "html.parser")
text = soup.get_text()
priceFix = text[2000:]
price = priceFix[priceFix.find("$"):priceFix.find("$")+10]
for i in range(5,10):
    try: 
        temp = int(price[i])
    except: 
        price = price[0:i]
name = text[9:text.find(")")+1]
unitFinder = soup.findAll("div", {"class": "product-information"})
unitFix = str(unitFinder)[113:]
for i in unitFix:
    if i not in ["<", '"', "'", "!", "/"]:
        unit += i 
    else: 
        break
#MarketFresh.sg
soup = BeautifulSoup(html, "html.parser")
text = soup.get_text()
priceFix = text[2000:]
price = priceFix[priceFix.find("$"):priceFix.find("$")+10]
for i in range(5,10):
    try: 
        temp = int(price[i])
    except: 
        price = price[0:i]P
name = text[18:text.find("|")-1]
'''
