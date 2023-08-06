import requests
import bs4
import lxml

def get_links(url):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 YaBrowser/23.5.3.904 Yowser/2.5 Safari/537.36"
    }
    
    r = requests.get(url, headers=headers).text

    soup = bs4.BeautifulSoup(r, 'lxml')

    # Список ссылок
    table_link = soup.find('div', class_='table-responsive')

    links = []
    names = []

    for a in table_link.find_all('a', href=True):
        links.append(a['href'])
        names.append(a.text)
    
    dictionary = {'Ссылки': links, 'Названия': names}

    return(dictionary)