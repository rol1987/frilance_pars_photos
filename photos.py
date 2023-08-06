import requests
import bs4
import lxml
import os
from pprint import pprint


def save_photos(link_list, name_folder):

    # Проверяем есть ли папка. Если нет - создаем её
    cwd = os.path.dirname(__file__)
    full_path = os.path.join(cwd, name_folder) 

    if not os.path.exists(full_path):
        print('Папка отсутствует')
        os.makedirs(full_path)
    else:
        print('Папка уже есть')

    # Пепебираем ссылки
    list_photos = []
    for link in link_list:
        print(link)
        headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaBrowser/23.5.3.904 Yowser/2.5 Safari/537.36"
        }
        
        r = requests.get(link, headers=headers).text

        soup = bs4.BeautifulSoup(r, 'lxml')

        # list_photos.append(soup.find_all('div', class_='mosaicflow__item'))
        
        immages = soup.find('div', class_='clearfix mosaicflow').find_all('img', src=True)

        list_immages = []

        for img in immages:
            list_immages.append(img['src'])
    
        pprint(list_immages)









