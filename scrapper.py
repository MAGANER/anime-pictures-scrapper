from bs4 import BeautifulSoup
import requests
import re


class Scrapper(object):
    def __init__(self,url):
        self.reg = r'"(.+?)"'
        
        self.page = requests.get(url)
        if self.page.status_code == 200:
            print("successfully connected to ",url)
            self.images = self.__load_images_urls(self.page)
            self.srcs = list(map(lambda n:self.__get_required_link(n),self.images))
            self.srcs = list(filter(lambda n:None != n,self.srcs))
            self.srcs = list(map(lambda n:"https://anime-pictures.net"+self.__extract_url(n),self.srcs))
            self.images = list(map(lambda n:self.__load_image(n),self.srcs))
        else:
            print("can't connect to ",url)
        
    def __get_required_link(self,link):
        return re.match(r"<.+by_tag=.+>",r"{}".format(link))
    def __extract_url(self,link):
        match = re.findall(self.reg,r'{}'.format(link.group()))
        return match[0]
    def get_images_srcs(self):
        return self.images
    def __load_images_urls(self,page):
        soup = BeautifulSoup(page.text, "html.parser")
        return soup.findAll("a")
    def __load_image(self,url):
        page = requests.get(url)
        if page.status_code == 200:
            print("sucessfully connected to ",url)
            soup = BeautifulSoup(page.text,"html.parser")
            data = soup.findAll("img",id="big_preview")
            src = "https:"+self.__get_src(data)
            return src
        else:
            print("can't connect to ",url)
    def __get_src(self,elem):
        match = re.search(r'src="(.+)"',r"{}".format(elem))
        return re.findall(self.reg,r'{}'.format(match.group()))[0]


    
