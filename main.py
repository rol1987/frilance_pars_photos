import photos
import first_requests


if __name__ == '__main__':

    # Параметры 'name_folder' и 'url' нужно задать вручную
    name_folder = 'ОБЪЕКТИВЫ'
    url = 'https://onfotolife.com/ru/lenses?lens=7artisans'
    
    link_list = first_requests.get_links(url)['Ссылки']
    name_list = first_requests.get_links(url)['Названия']
    # print(link_list)
    # print(name_list)

    photos.save_photos(link_list, name_list, name_folder)

