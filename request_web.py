import grequests
import requests
import bs4
import lxml
import os
from pprint import pprint
from io import BytesIO
from PIL import Image
import work_with_photos
import time
import datetime


def responses(links, name_list, name_folder):
    
    # Проверяем есть ли папка. Если нет - создаем её
    cwd = os.path.dirname(__file__)
    full_path = os.path.join(cwd, name_folder) 

    if not os.path.exists(full_path):
        print('Папка отсутствует')
        os.makedirs(full_path)
    else:
        print('Папка уже есть')

    sites = links
    
    response = (grequests.get(url) for url in sites)
    resp = grequests.map(response)
    print(resp)

    # Запускаем цикл и проходим по первичным ссылкам
    stranica = 0
    for r in resp:
        
        
        ind = 1
        number_pages = 1
        next_page = r.url
        pages_list = []

        pages_list.append(next_page)
        while ind == 1:
            
            next_page = next_page.replace(f'page={number_pages}', f'page={number_pages + 1}')
            
            print('Пробуем подключиться к странице: ', next_page)

            r1 = requests.get(next_page)
            if r1.status_code == 200:
                soup = bs4.BeautifulSoup(r1.text, 'lxml')
                
                find_next_page = soup.find('a', {'href': {next_page}})
                if find_next_page != None:
                    if int(find_next_page.text) == number_pages + 1:
                        pages_list.append(next_page) # Список ссылок на внутренние страницы
                        
                        number_pages += 1
                        ind = 1
                    else:
                        ind = 0
                else:
                    ind = 0
            else:
                ind = 0
    
        
        response = (grequests.get(url) for url in pages_list)
        resp_pages_list = grequests.map(response)
        
        list_img_link = []
        for rpl in resp_pages_list:
            soup_rpl = bs4.BeautifulSoup(rpl.text, 'lxml')            
            count_photo = 0
            for l in soup_rpl.find('div', class_='clearfix mosaicflow').find_all('a', class_='fancyimage'):
                count_photo += 1
                list_img_link.append(l['href']) # Список, в котором хранятся ссылки на все фотографии подраздела
            print(f'На странице {count_photo} фотографий')

        # Перебираем список и сохраняем фотографии
        k = 0
        dict_foto_width = {}
        dict_foto_height = {}
        
        for url in list_img_link:
            k += 1
            headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaBrowser/23.5.3.904 Yowser/2.5 Safari/537.36"
            }
            image = requests.get(url, headers=headers).text
            soup_photo = bs4.BeautifulSoup(image, 'lxml')
            link_photo = soup_photo.find('div', class_='text-center').find('img')['src']
        
            # Подключаемся к фото и сохраняем его
            img_data = requests.get(link_photo, headers=headers).content
            full_path_img = os.path.join(full_path, f'{name_list[stranica]}_{k}.jpg')
            with open(full_path_img, 'wb') as handler:
                    handler.write(img_data)

            # Определяем ширину и высоту и записываем их в словари
            im = Image.open(full_path_img)
            width = im.width
            height = im.height
            im.close()

            if width > height:
                dict_foto_width[full_path_img] = width
            else:
                dict_foto_height[full_path_img] = height

            # Сортируем
            sorted_dict_foto_width = {}
            sorted_keys = sorted(dict_foto_width, key=dict_foto_width.get)
            for w in sorted_keys:
                sorted_dict_foto_width[w] = dict_foto_width[w]

            sorted_dict_foto_height = {}
            sorted_keys = sorted(dict_foto_height, key=dict_foto_height.get)
            for w in sorted_keys:
                sorted_dict_foto_height[w] = dict_foto_height[w]
            
            time.sleep(0.1)
         
            
        # Удаляем ненужные фото и оставляем 3 самих горизонтальных
        while len(sorted_dict_foto_width) > 3:
            indexToBeRemoved = 0
            os.remove(list(sorted_dict_foto_width.keys())[indexToBeRemoved])
            sorted_dict_foto_width.pop(list(sorted_dict_foto_width.keys())[indexToBeRemoved])
            time.sleep(1)
        
        # Удаляем ненужные фото и оставляем 3 самих вертикальных
        while len(sorted_dict_foto_height) > 3:
            indexToBeRemoved = 0
            os.remove(list(sorted_dict_foto_height.keys())[indexToBeRemoved])
            sorted_dict_foto_height.pop(list(sorted_dict_foto_height.keys())[indexToBeRemoved])
            time.sleep(1)
        stranica += 1   