import requests
import random
from bs4 import BeautifulSoup
global i, out


def parse(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 YaBrowser/19.10.2.195 Yowser/2.5 Safari/537.36'}

    html = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'lxml')

    img_tag = soup.find('img', {'id': 'screenshot-image'})
    if img_tag == None:
        main()
    else:
        photo_url = img_tag['src']
        try:
            photo = requests.get(photo_url, headers=headers).content
        except requests.exceptions.MissingSchema:
            photo_url_one = "http:" + photo_url
            photo = requests.get(photo_url_one, headers=headers).content

        return photo
def name_generator(gen):
    global out
    out = 'output'+"_"+gen+'.png'
    return out

def generator():
    global gen
    chars = 'abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

    number = 1
    length = 10
    for n in range(number):
        gen = ''
        for i in range(length):
            gen += random.choice(chars)
        print(gen)
    return gen
def main():

    generator()
    url = "https://prnt.sc/" + gen
    url = str(url)
    print(url)

    photo = parse(url)

    name_generator(gen)
    if photo == None:
        print("нет фотки")
        main()
    else:
     with open(out, 'wb') as f:
            f.write(photo)

for x in range(400):
    main()
