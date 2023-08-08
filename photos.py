import requests
import bs4
import lxml
import os
from pprint import pprint
from io import BytesIO
from PIL import Image
import work_with_photos


def save_photos(link_list, name_list, name_folder):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaBrowser/23.5.3.904 Yowser/2.5 Safari/537.36"
    }

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
    n = 0
    ind = 1
    for link in link_list:
        print(link)
        headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaBrowser/23.5.3.904 Yowser/2.5 Safari/537.36"
        }
        
        r = requests.get(link, headers=headers).text

        soup = bs4.BeautifulSoup(r, 'lxml')

        # Список ссылок на фотографии
        # immages = soup.find('div', class_='clearfix mosaicflow').find_all('img', src=True)

        list_immages_link = [] # Список для наполнения ссылками на фотографии

        # Пробегаюсь по списку и ищу тэги src
        for img in soup.find('div', class_='clearfix mosaicflow').find_all('a', class_='fancyimage'):
            # print(type(img))
            list_immages_link.append(img['href'])

        k = 0
        dict_photo_vertical = {'ширина': '', 'высота': '', 'название_фотографии': ''} # Создаем словарь, в который будем заносить параметры вертикальных фотографии
        dict_photo_horizontal = {'ширина': '', 'высота': '', 'название_фотографии': ''} # Создаем словарь, в который будем заносить параметры горизонтальных фотографии

        list_width_photo_vertical = [] # Список ширины
        list_height_photo_vertical = [] # Список высоты
        list_name_photo_vertical = [] # Список названий


        list_width_photo_horizontal = [] # Список ширины
        list_height_photo_horizontal = [] # Список высоты
        list_name_photo_horizontal = [] # Список названий
        full_list_name_photo = []

        final_dict_horizontal = {}
        final_dict_vertical = {}
        
        for img in list_immages_link:
            try:
                k += 1
                image = requests.get(img, headers=headers).text
                soup_photo = bs4.BeautifulSoup(image, 'lxml')
                link_photo = soup_photo.find('div', class_='text-center').find('img')['src']
            
            
                img_data = requests.get(link_photo, headers=headers).content
                name = name_list[n].replace("/", "_")
                
                full_path_img = os.path.join(full_path, f'{name}_{k}.jpg')
                
                with open(full_path_img, 'wb') as handler:
                    handler.write(img_data)   

                im = Image.open(full_path_img)
                width = im.width
                height = im.height

                full_list_name_photo.append(full_path_img)

                
                
                # print(width, '////////', height, '////////', full_path_img)
                def append_horizontal():
                    list_width_photo_horizontal.append(width)
                    list_height_photo_horizontal.append(height)
                    list_name_photo_horizontal.append(full_path_img)
                    dict_photo_horizontal['ширина'] = list_width_photo_horizontal
                    dict_photo_horizontal['высота'] = list_height_photo_horizontal
                    dict_photo_horizontal['название_фотографии'] = list_name_photo_horizontal
                    final_dict_horizontal[full_path_img] = width

                def append_vertical():
                    list_width_photo_vertical.append(width)
                    list_height_photo_vertical.append(height)
                    list_name_photo_vertical.append(full_path_img)
                    dict_photo_vertical['ширина'] = list_width_photo_vertical
                    dict_photo_vertical['высота'] = list_height_photo_vertical
                    dict_photo_vertical['название_фотографии'] = list_name_photo_vertical
                    final_dict_vertical[full_path_img] = height

                if width > height:
                    if len(list_width_photo_horizontal) == 0:
                        append_horizontal()
                    else:
                        if list_width_photo_horizontal[-1] > width:
                            append_horizontal()
                else:
                    if len(list_height_photo_vertical) == 0:
                            append_vertical()
                    else:        
                        if list_height_photo_vertical[-1] > height:
                            append_vertical()

                print(dict_photo_horizontal, dict_photo_vertical)
                print()
            except:
                pass
            
    
        work_with_photos.delete_photo(dict_photo_horizontal, dict_photo_vertical, final_dict_vertical, final_dict_horizontal, full_list_name_photo)
        n += 1
        










