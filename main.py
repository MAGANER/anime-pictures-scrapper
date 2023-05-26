from scrapper import Scrapper
from PIL import Image
import random
import requests
import re
import os

def get_images_from_website(url):
    scrapper = Scrapper(url)
    return scrapper.get_images_srcs()
def get_image(url,path_to_save):
    im = Image.open(requests.get(url, stream=True).raw)
    rgb_im = im.convert('RGB')
    rgb_im.save(path_to_save,"JPEG")
    
def scrap_website():
    page_number = random.randint(0,2218)
    url = "https://anime-pictures.net/pictures/view_posts/{}?search_tag=light+erotic&lang=en".format(page_number)
    src = get_images_from_website(url)
    pic_number = int(input("how many pictures you want to fetch?"))
    directory = r'{}'.format(input("directory to store them:"))
    if not os.path.exists(directory):
        os.makedirs(directory)
    if pic_number > len(src):
       pic_number = len(src)-1
    for n in range(pic_number):
       get_image(random.choice(src),directory+"/img"+str(n)+".jpg")
    

if __name__ == "__main__":
    scrap_website()


