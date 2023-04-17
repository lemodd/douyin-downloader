import json
import requests
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# GET URLS

# Open Console

# var vids = [];

# var li = document.querySelectorAll('li a');

# li.forEach((v, i) => vids.push({'url': 'https://www.douyin.com' + v.getAttribute('href')}))

# vids

# Right Click + Copy Object => Paste to list.json => Remove unused links

def main() -> None:
    name = input("Name of user: ")
    print("Create folder by name: " + name)
    order = input("Order from (top|bottom): ")
    if order != 'top' and order != 'bottom':
        print('Wrong order format')
        return
    print("Download from: " + name)
    with open('list.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    short_data = []
    i = 0
    for video in data:
        short_data.append({'id': i, 'url': video['url']})
        i+=1
    with open('src.json', 'w', encoding='utf-8') as f:
        json.dump(short_data, f, indent=2)
    data = short_data
    if order == 'bottom':
        data.reverse()
    
    op = webdriver.ChromeOptions()
    op.add_argument
    ("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    +"AppleWebKit/537.36 (KHTML, like Gecko)"
    +"Chrome/87.0.4280.141 Safari/537.36")

    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    j = 0
    for dat in tqdm(data):
        driver.get(dat['url'])
        element = driver.find_element(By.CSS_SELECTOR, 'source')
        src = element.get_attribute('src')
        time.sleep(3)
        res = requests.get(src, stream=True)
        isExist = os.path.exists(f'download/{name}')
        if not isExist:
            os.makedirs(f'download/{name}')
        with open(f'download/{name}/{j}.mp4', 'wb') as f:
            for chunk in res.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
        j+=1
    driver.close()


if __name__ == '__main__':
    main()
