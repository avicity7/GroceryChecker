from urllib.request import Request, urlopen
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import gui
import sys


prices = []
names = []
units = [] 

# The explanation of how we find the product's name, quantity, price and link is explained on the first storeSearch function
# The remaining functions do not have much explanation as the method is the same but have been hardcoded for specific websites

def storeSearch(searchString,fairpricePrice,fairpriceUnit):
    
    fairpricePrice = fairpricePrice[1:]
    stores = ["Cold Storage","Dei","Giant"]
    #Cold Storage Search
    try:
        lst = [] 
        temp = 0
        sep = "+"
        coldSearch = searchString.split()
        coldSearch = sep.join(coldSearch) # Obtaining the URL of the item that is being searched using the website's syntax
        url = Request('https://coldstorage.com.sg/search?q=' + coldSearch, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(url)
        #Getting item parameters
        productUnit = ""
        brandName = str()
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text() # We scrape the HTML of the website and store it's data into variables
        unitFinder = soup.findAll("span", {"class": "size"}) # We scope down the HTML to search for the information we want
        priceFinder = soup.findAll("div", {"class": "content_price"})
        number = int()
        price = str()
        sw = 0
        coldProductName = str()
        temp = str() 
        decimal = str()
        priceFinder = str(priceFinder[0])

        for i in range(0,len(priceFinder)): # Function to find the price of the product
            try:
                number = int(priceFinder[i])
                if sw == 1:
                    price += str(number)
                
            except: # Ensuring that only the price is found and not any characters from HTML. Addition of decimal point also
                if priceFinder[i] == "$":
                    sw = 1
                elif priceFinder[i] == "." and sw == 1: 
                    price += priceFinder[i]
                elif priceFinder[i] == "<" and sw == 1:
                    break 
                else: 
                    continue

        brandFinder = soup.findAll("div", {"class": "product_category_name"}) # Finding the brand of the product
        brandFinder = str(brandFinder[0])
        brand = str()
        for i in range(0,len(brandFinder)):
            try:
                if brandFinder[i] + brandFinder[i+1] + brandFinder[i+2] == "<b>":
                    for i in range(i+3,len(brandFinder)):
                        if brandFinder[i] == "<":
                            break 
                        else: 
                            brand+= brandFinder[i]
            except: 
                break

        nameFinder = soup.findAll("div", {"class": "product_category_name"}) # Finding the name of the product from the HTML
        nameFinder = str(nameFinder[0])
        nameFinder = nameFinder.split()
        exceptions = ['"',",","<",">"]
        name = str()
        nameSw = 0
        for x in nameFinder: 
            nameSw = 0
            for y in x: 
                if y in exceptions: # Filtering out any HTML syntax
                    nameSw = 1
            if nameSw == 0: 
                name += x 
                name += " "

        unitFinder = str(unitFinder[0]) # Finding the quantity and the unit of the product that is being searched
        unitFinder = unitFinder.split() 
        unitFinder = unitFinder[-1]
        unit = str()
        for i in range(0,len(unitFinder)):
            if unitFinder[i] == "<": # Filtering out any HTML syntax
                break
            else: 
                unit += unitFinder[i]

        coldProductName = brand + " " + name # Assigning the details of the items to the respective stores' variables
        coldPrice = price 
        coldProductUnit = unit
    except: 
        coldProductName =  "9999"
        coldPrice = "9999" 
        coldProductUnit = "9999"
    
    #Dei Store Search
    try:
        sep = "+"
        deiSearch = searchString.split()
        deiSearch = sep.join(deiSearch) # Link finder
        product = str()
        session = HTMLSession()
        r = session.get('https://www.dei.com.sg/search?_token=aRkpJ3nCKN5iArm0CpLMEz0gBtxPYF5DyPrk36T6&search='+deiSearch)
        links = r.html.links
        e = [x for x in links]
        for y in e:
            try:
                if y[40]+y[41]+y[42]+y[43]+y[44]+y[45]+y[46]+y[47] == "/product":
                    product = y
                    break
            except:
                continue
        url = Request(product, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(url)
        html = page.read().decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text() # Storing HTML
        priceFinder = soup.findAll("span", {"class": "text-price"})
        priceFinder = str(priceFinder[0])
        priceFinder = priceFinder[10:]
        sw = 0
        price = str() # Price finder
        for i in range(0,len(priceFinder)): # HTML syntax filter
            if sw == 1: 
                if priceFinder[i] == "<":
                    break
                else: 
                    price+=priceFinder[i]
            elif priceFinder[i] == ">":
                sw = 1
        name = text[9:text.find("|")-1]
        nom = name.split(" - ")
        weight = nom[-1]

        deiPrice = price 
        deiProductName = name
        deiProductWeight = weight
    except:
        deiPrice = "9999"
        deiProductName = "9999"
        deiProductWeight = "9999"
    
    #Giant Store Search 
    try:
        sep = "+"
        giantSearch = searchString.split()
        giantSearch = sep.join(giantSearch) # Link finder
        url = Request("https://giant.sg/search?q="+giantSearch, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(url)
        #Getting item parameters
        productUnit = ""
        brandName = str()
        html_bytes = page.read()
        html = html_bytes.decode("utf-8")
        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text() # Storing HTML


        number = int() 
        price = str() 
        sw = 0
        coldProductName = str()
        temp = str() 
        decimal = str()
        unitFinder = soup.findAll("span", {"class": "size"})
        priceFinder = soup.findAll("div", {"class": "content_price"})
        if priceFinder == []: 
            priceFinder = priceFinder = soup.findAll("div", {"class": "price_now price_normal price-off-normal-price"}) # Price finder
        priceFinder = str(priceFinder[0])

        for i in range(0,len(priceFinder)): # HTML syntax filter
            try:
                number = int(priceFinder[i])
                if sw == 1:
                    price += str(number)
                
            except: 
                if priceFinder[i] == "$":
                    sw = 1
                elif priceFinder[i] == "." and sw == 1: 
                    price += priceFinder[i]
                elif priceFinder[i] == "<" and sw == 1:
                    break 
                else: 
                    continue

        brandFinder = soup.findAll("a", {"class": "to-brand-page"}) # Brand finder
        brandFinder = str(brandFinder[0])
        brandFinder = brandFinder[10:]
        brand = str()
        sw = 0
        for i in range(0,len(brandFinder)): # HTML syntax filter
                if sw == 1: 
                    if brandFinder[i] == "<":
                        break
                    else: 
                        brand += brandFinder[i]
                elif brandFinder[i] == ">":
                    sw = 1 
                    


        nameFinder = soup.findAll("a", {"class": "product-link"}) # Name finder
        nameFinder = str(nameFinder[0])
        nameFinder = nameFinder[10:]
        name = str()
        sw = 0
        for i in range(0,len(nameFinder)): # HTML syntax filter
                if sw == 1: 
                    if nameFinder[i] == "<":
                        break
                    else: 
                        name += nameFinder[i]
                elif nameFinder[i] == ">":
                    sw = 1 

        unitFinder = str(unitFinder[0]) # Unit filter
        unitFinder = unitFinder.split() 
        unitFinder = unitFinder[-1]
        unit = str()
        for i in range(0,len(unitFinder)): # HTML syntax filter
            if unitFinder[i] == "<":
                break
            else: 
                unit += unitFinder[i]

        giantProductUnit = unit # Finalising variables
        giantProductName = name 
        giantProductPrice = price
    except:
        giantProductUnit = "9999"
        giantProductName = "9999"
        giantProductPrice = "9999"
    # Appending parameters to lists for comparison
    prices.append(coldPrice);prices.append(deiPrice);prices.append(giantProductPrice)
    names.append(coldProductName);names.append(deiProductName);names.append(giantProductName)
    units.append(coldProductUnit);units.append(deiProductWeight);units.append(giantProductUnit)
    for i in range(0,len(units)):
        units[i] = str(units[i]).replace(" ","")
    
    
    while True:
        lowestpricelist = ''
        lowest = float(fairpricePrice)
        lowestIndex = 4
        sameIndex = []
        for i in range(0,len(prices)): # Price comparison from various stores
            if float(prices[i]) < lowest: 
                lowest = float(prices[i])
                lowestIndex = i
            elif float(prices[i]) == lowest:
                sameIndex.append(i)
                
        if lowestIndex == 4: # Printing the store which has the lowest price as well as the price
            gui.sg.popup("\nThe cheapest place to get this item is from FairPrice: ${price}".format(price = fairpricePrice))

            for i in sameIndex:
                lowestpricelist += ("\n{store} has the item at the same price: ${price}".format(store = stores[i],price = prices[i]))
        
            break
            if lowestpricelist != '':
                gui.sg.popup(lowestpricelist)
        
        elif len(sameIndex) >= 1:
            if units[lowestIndex].lower() == fairpriceUnit.lower():
                gui.sg.popup("\nThe cheapest place to get this item is from {store}: ${price}".format(store = stores[lowestIndex], price = prices[lowestIndex]))
                for i in sameIndex:
                    lowestpricelist += ("\n{store} has the item at the same lowest price: ${price}".format(store = stores[i],price = prices[i]))
                if lowestpricelist != '':
                    gui.sg.popup(lowestpricelist)
            else: 
                del prices[lowestIndex]
                del names[lowestIndex]
                del units[lowestIndex]
                del stores[lowestIndex]
                continue
            break
            
        elif units[lowestIndex].lower() == fairpriceUnit.lower():
            gui.sg.popup("\nThe cheapest place to get this item is from {store}: ${price}".format(store = stores[lowestIndex], price = prices[lowestIndex]))
            break
                                
        else: 
            del prices[lowestIndex]
            del names[lowestIndex]
            del units[lowestIndex]
            del stores[lowestIndex]
        
    return ""
    

extraLinks = []
session = HTMLSession()
gui.Mainpage()
prevtext = '-'
while True:
    
    inp = gui.textin
    
    if inp == prevtext:
        inp = gui.sg.popup_get_text("Please enter another item as specifcally as possible: ")
        
        if inp in ("","Cancel",gui.sg.WIN_CLOSED):
            sys.exit()
    
        
    sep = "%20"
    inp = inp.split()
    inp = sep.join(inp)
    try:
        #Getting item links from Fairprice search page to see whether product is there or not
        r = session.get('https://www.fairprice.com.sg/search?query=' + inp)
        links = r.html.links
        e = [x for x in links]
        for y in e:
            try:
                if y[0]+y[1]+y[2]+y[3]+y[4]+y[5]+y[6]+y[7] == "/product":
                    product = y
                    break
                else:
                    product = ""
            except:
                continue
        if product == "":
            raise ValueError
        url = Request('https://www.fairprice.com.sg' + product, headers={'User-Agent': 'Mozilla/5.0'})
        page = urlopen(url)
        #Getting item parameters (similar to storeSearch function)
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

        inp = gui.sg.popup_yes_no("\nItem found: {productname} {productunit} {cost}".format(productname = productName, productunit = productUnit, cost = price)+"\nIs this the item that you were looking for?").lower()
        
        #When item found is accepted by user: 
        if inp == "yes":
            search = productName +" " + productUnit
            try:
                gui.sg.popup(storeSearch(search,price,productUnit))
                prices = []
                names = []
                units = []
                stores = ["Cold Storage","Dei","Giant"]
            except:
                gui.sg.popup("Sorry, we could not find this item on other stores.")
        #When item found is rejected by user, going through top 5 results in Fairprice search: 
        elif inp == "no":
            gui.sg.popup("Alright! We'll display the other top 5 search results:")
            try:
                productlist = ''
                for times in range (1,6):
                    e.remove(product)
                    for y in e:
                        try:
                            if y[0]+y[1]+y[2]+y[3]+y[4]+y[5]+y[6]+y[7] == "/product": # Finding details on top 5 products shown
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
                                productlist += ("\n{time}. {productname} {productunit} {cost}".format(time = times, productname = productName, productunit = productUnit, cost = price))
                                break
                        except:
                            continue
            except:
                print("")
            gui.sg.popup_scrolled(productlist, no_titlebar = True)
            inp = gui.sg.popup_get_text("Which of these are what you are looking for? Enter 0 if it is none of them, else enter the number of the item: ")
            if inp == "0":
                continue
            #If one of the 5 links has been selected; we find details of that product
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
                try:
                    print(storeSearch(search,price,productUnit))
                    prices = []
                    names = []
                    units = []
                    stores = ["Cold Storage","Dei","Giant"]
                except: 
                    gui.sg.popup("Sorry, we could not find that item in other stores.")
        prevtext = gui.textin
                          
    except:
        prevtext = gui.textin
        gui.sg.popup("Sorry, we are not able to find that item. Please enter a different item or name.")
        continue
