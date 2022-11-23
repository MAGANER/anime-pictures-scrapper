from bs4 import BeautifulSoup
import requests
import re


class Scrapper(object):
    def __init__(self,url):
        self.page = requests.get(url)
        if self.page.status_code == 200:
            print("successfully connected to ",url)
            self.images = self.__load_images(self.page)
            self.srcs = list(map(lambda img: self.__get_img_src(img),self.images))
        else:
            print("can't connect to ",url)
        

    def get_images_srcs(self):
        return self.srcs
    def __load_images(self,page):
        soup = BeautifulSoup(page.text, "html.parser")
        return soup.findAll("img")
    def __get_img_src(self,img_str):
        match = re.search(r'src=".+"',r"{}".format(img_str))
        return match.group()
