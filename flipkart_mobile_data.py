import requests
from bs4 import BeautifulSoup
import pandas as pd

#url = "https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DRealme&otracker=nmenu_sub_Electronics_0_Realme&page=1"
#r = requests.get(url)
#print(r)
#soup = BeautifulSoup(r.text, "lxml")

#product = soup.find_all('div', class_ = "RG5Slk")
products = []
#for pr in product:
 #   products.append(pr.text)
#print(products)

price = []
#prices = soup.find_all('div',class_ = "hZ3P6w DeU9vF")
#print(prices)
#for rs in prices:
 #   price.append(rs.text)
#print(price)

ratings = []
#rating = soup.find_all('div',class_ = "MKiFS6")
#for rate in rating:
#    ratings.append(rate.text)
#print(ratings)
#print(len(products))
#print(len(price))
#print(len(ratings))

for i in range(2,9):
    url = "https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.brand%255B%255D%3DRealme&otracker=nmenu_sub_Electronics_0_Realme&page="+str(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.text,"lxml")
    product = soup.find_all('div', class_="RG5Slk")
    for pr in product:
        products.append(pr.text)
    print(products)


    prices = soup.find_all('div', class_="hZ3P6w DeU9vF")
    # print(prices)
    for rs in prices:
        price.append(rs.text)
    print(price)


    rating = soup.find_all('div', class_="MKiFS6")
    for rate in rating:
        ratings.append(rate.text)
    print(ratings)
    print(len(products))
    print(len(price))
    print(len(ratings))

    #np = soup.find('a',class_ = "jgg0SZ")
    #np1 = np.get("href")
    #cnp = "https://www.flipkart.com/" + np1
    #print(cnp)
df = pd.DataFrame({"Product name": products, "Price":price,"Review out of 5": ratings})
print(df)

df.to_csv("Flipkart_Mobile_Detail.csv")
