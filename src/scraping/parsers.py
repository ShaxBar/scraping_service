import requests
import codecs
from bs4 import BeautifulSoup as BS
from random import randint

__all__ = ('work', 'rabota')

header = [{'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
          {
              'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36',
              'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'},
          {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:53.0) Gecko/20100101 Firefox/53.0',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}]


def work(url, city=None, language=None):
    jobs = []
    errors = []
    if url:
        resp = requests.get(url, headers=header[randint(0, 2)])

        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            main_div = soup.find('div', id="a11y-main-content")
            if main_div:
                div_list = main_div.find_all('div', attrs={
                    'class': 'vacancy-search-item__card serp-item_link vacancy-card-container--OwxCdOj5QlSlCBZvSggS vacancy-card_clickme--Ti9glrpeP1wwAE3hAklj'})
                for div in div_list:
                    title = div.find('h2')
                    href = title.a['href']
                    company = 'No name'
                    logo = div.find('img')
                    if logo:
                        company = logo['alt']
                    jobs.append({'title': title.text, 'url': href,
                                 'company': company,
                                 'city_id': city, 'language_id': language})
            else:
                errors.append({'url': url, 'title': "Div does not exists"})
        else:
            errors.append({'url': url, 'title': "Page do not response"})
        return jobs, errors


def rabota(url, city=None, language=None):
    jobs = []
    errors = []
    if url:
        resp = requests.get(url, headers=header[randint(0, 2)])

        if resp.status_code == 200:
            soup = BS(resp.content, 'html.parser')
            main_div = soup.find('div', attrs={'class': 'default-grid__content'})
            if main_div:
                div_list = main_div.find_all('div', attrs={'class': 'snippet__inner'})
                for div in div_list:
                    title = div.find('h2')
                    href = title.a['href']
                    company = 'No name'
                    ul = div.find('span', attrs={'class': 'snippet__meta-value'})
                    if ul:
                        company = ul.text
                    jobs.append({'title': title.text, 'url': href,
                                 'company': company,
                                'city_id': city, 'language_id': language})
            else:
                errors.append({'url': url, 'title': "Div does not exists"})
        else:
            errors.append({'url': url, 'title': "Page do not response"})
        return jobs, errors


if __name__ == '__main__':
    url = 'https://www.rabota.ru/companies/search/?query=python&regionList%5B%5D=3'
    jobs, errors = rabota(url)
    h = codecs.open('../work.json', 'w', 'utf-8')
    h.write(str(jobs))
    h.close()
