from bs4 import BeautifulSoup as soup
import requests
import re
from user_agent import generate_user_agent
import random

class Scrapper(object):
    def __gen_headers(self):
        return {'User-Agent': generate_user_agent(device_type="desktop", os=('mac', 'linux'))}
    def __init__(self,url):
        self.reg = r'"(.+?)"'
        
        self.headers = self.__gen_headers()
        self.page = requests.get(url,timeout=20,headers=self.headers,verify=False)
        self.__target_srcs = []
        if self.page.status_code == 200:
            print("successfully connected to ",url)

            links = self.get_links()#fetch links, containing required data

            #get random 
            random_ids = [random.randint(0,len(links)-1) for _ in range(len(links))]
            for i in random_ids:
                try:
                    self.page = requests.get(links[i],timeout=5,headers=self.__gen_headers())
                except Exception as e:
                    print("can not catch {} !".format(links[i]))
                finally:
                    if self.page.status_code == 200:
                        s = soup(self.page.content,"html.parser")
                        target = s.find("img",id="big_preview")
                        self.__target_srcs.append("https://"+target["src"][2:])
                        
        else:
            print("can't connect to ",url)
            exit(-1)

    def get_links(self):
        s = soup(self.page.content,"html.parser")
        links = s.find_all(["a"])
        links = list(filter(lambda n:"/posts/" in n["href"],links))
        return list(map(lambda n:"https://anime-pictures.net"+n["href"],links))

    def get_images_srcs(self):
        return self.__target_srcs

        

    
