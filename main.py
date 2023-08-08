import request_web
import first_requests


if __name__ == '__main__':

    # Параметры 'name_folder' и 'url' нужно задать вручную
    name_folder = 'ОБЪЕКТИВЫ'
    url = 'https://onfotolife.com/ru/cameras?type=compact&camera=Genius'
    
    link_list = first_requests.get_links(url)['Ссылки']
    name_list = first_requests.get_links(url)['Названия']

    request_web.responses(link_list, name_list, name_folder)
