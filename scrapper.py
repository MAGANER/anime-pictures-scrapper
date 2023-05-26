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

            s = soup(self.page.content,"html.parser")
            tags = s.find_all(["a"])
            tags = list(filter(lambda n:"/posts/" in n["href"],tags))
            tags =list(map(lambda n:"https://anime-pictures.net"+n["href"],tags))

            
           
            random_ids = [random.randint(0,len(tags)-1) for _ in range(len(tags))]
            for i in random_ids:
                try:
                    self.page = requests.get(tags[i],timeout=5,headers=self.__gen_headers())
                except Exception as e:
                    print("can not catch {} !".format(tags[i]))
                finally:
                    if self.page.status_code == 200:
                        s = soup(self.page.content,"html.parser")
                        target = s.find("img",id="big_preview")
                        self.__target_srcs.append("https://"+target["src"][2:])
                        
        else:
            print("can't connect to ",url)
            exit(-1)

    def get_images_srcs(self):
        return self.__target_srcs

        

    
