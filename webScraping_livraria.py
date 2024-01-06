from bs4 import BeautifulSoup as bs
import requests

url = 'https://estivalet.github.io/static-testing-sites/bookdepository'
resposta = requests.get(url)
# print(resposta.status_code)

html = resposta.content
soup = bs(html, 'lxml') # O lxml é um parser que se adapta melhor a páginas maiores e mais complexas.

# tagH3 = soup.find_all('h3', class_ = "title")
# for h3 in tagH3:
    # print(h3.get_text(strip = True))

infosLivros = soup.find_all('div', class_ = 'book-item')
for info in infosLivros:
    print('Título: ' + info.find('h3').get_text(strip = True))
    print('Autor: ' + info.find('p', class_ = 'author').get_text(strip = True))
    print('Publicado em: ' + info.find('p', class_ = 'published').get_text(strip = True))
    print('Formato: ' + info.find('p', class_ = 'format').get_text(strip = True))
    precoOriginal = info.find('span', class_= 'rrp')
    precoAtual = info.find('p', class_ = 'price')
    if not precoAtual:
        print('Preço: Fora de estoque.')
    else:
        if precoOriginal:
            print('Preço original: ' + precoOriginal.get_text(strip = True))
            print('Preço atual: ' + precoAtual.get_text(strip = True).split('R$')[1])
        else:
            print('Preço: R$' + precoAtual.get_text(strip = True).split('$')[1])
    print('---------------------')