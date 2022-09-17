import  requests
from bs4 import BeautifulSoup
import lxml
from time import sleep

#list_card_url=[] это если немного страниц
headers={"User-Agent":"Mozilla/5.0(Windows; U; Windows NT 6.1; en-US; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5 (.NET CLR 3.5.30729)"}


def download(url):
    resp=requests.get(url,stream=True)
    r=open("C:\\Users\\user\\imag\\"+url.split("/")[-1],"wb")
    for value in resp.iter_content(1024*1024):
        r.write(value)
    r.close()


def get_url():
    for count in range(1,8):
        sleep(1)
        URL='https://scrapingclub.com/exercise/list_basic/?page=1}'
        response = requests.get(URL,headers=headers)
#print(response.text)
        soup=BeautifulSoup(response.text, "lxml")
#print(soup)
        data=soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")
#print(data)
        for i in data:
        #name = i.find("h4", class_="card-title").text.data=soup.find_all("div", class_="col-lg-4 col-md-6 mb-4")replace("\n","")
#print(name)
       # price = i.find("h5").text
#print(price)
       # url_img="https://scrapingclub.com"+i.find("img", class_="card-img-top img-fluid").get("src")
            card_url = "https://scrapingclub.com" + i.find("a").get("href")#идем во внутрь
        #print(name+"\n"+price+"\n"+url_img+"\n\n")
            yield(card_url)


def array():
    for card_url in get_url():
     #   sleep(1)
        response=requests.get(card_url,headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find("div", class_="card mt-4 my-4")
        name = data.find("h3", class_="card-title").text
        price = data.find("h4").text
        text = data.find("p",class_="card-text").text
        url_img = "https://scrapingclub.com" + data.find("img", class_="card-img-top img-fluid").get("src")
        #print(name + "\n" + price + "\n" + text+"\n"+url_img + "\n\n")
        download(url_img)
        yield name,price ,text,url_img
