import links
import photos


if __name__ == '__main__':

    # Параметры 'name_folder' и 'url' нужно задать вручную
    name_folder = 'ОБЪЕКТИВЫ'
    url = 'https://onfotolife.com/ru/lenses?lens=7artisans'
    
    link_list = links.get_links(url)

    photos.save_photos(link_list, name_folder)

