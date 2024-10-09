import requests
from bs4 import BeautifulSoup
import json


def importar_noticias(url, id_serie):
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    noticias = [noticia.find_next('a').text for noticia in soup.find_all('h2', attrs={'class': 'meta-title'})]
    links = ['https://www.adorocinema.com' + noticia.find('a')['href'] for noticia in
             soup.find_all('h2', attrs={'class': 'meta-title'})]
    datas = [noticia.text for noticia in soup.find_all('div', attrs={'class': 'meta-date'})]
    categorias = [noticia.text for noticia in soup.find_all('div', attrs={'class': 'meta-category'})]

    noticia_dict = [
        dict({
            'titulo': noticia,
            'link': links[i],
            'data': datas[i],
            'categorias': categorias[i],
            'serie': {'$oid': id_serie}
        })
        for i, noticia in enumerate(noticias)
    ]

    noticia_json = json.dumps(noticia_dict)

    print(noticia_json)
    return noticia_json


def importar_serie(url, elenco):
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    title = soup.find('h1', {'class': 'item'}).text.strip()
    description = soup.find('div', {'class': 'content-txt'}).text.strip()
    rating = soup.find('span', {'class': 'stareval-note'}).text.strip()
    genres = [genre.text.strip() for genre in soup.find_all('div', {'class': 'entity-card'})[0].find_next('div', attrs={
        'class': 'meta-body-item'}).find_all('span')[-2:]]
    pais = soup.find('div', attrs={'class': 'meta-body-nationality'}).find_next('span', attrs={
        'class': 'nationality'}).text.strip()
    ano = soup.find_all('div', {'class': 'entity-card'})[0].find_next('div',
                                                                      attrs={'class': 'meta-body-info'}).find_next(
        'span').previous_sibling.strip()
    produtores = [produtor.text.strip() for produtor in
                  soup.find_all('div', {'class': 'meta-body-direction'})[0].find_all('a', attrs={'class': 'blue-link'})]

    ### Elenco:
    url_elenco = f'{url}{elenco}'
    response = requests.get(url_elenco)
    elenco = BeautifulSoup(response.content, 'html.parser')

    atores = [ator.text.strip() for ator in elenco.find_all('a', {'class': 'meta-title-link'})]
    personagens = [personagem.text.replace('Personagem :', '').strip() for personagem in
                   elenco.find_all('div', {'class': 'meta-sub light'})]
    atores_personagens = [dict({'nome': ator, 'personagem': personagens[i]}) for i, ator in enumerate(atores)]

    ### Crítica
    url = f'{url}criticas'
    response = requests.get(url)
    critica = BeautifulSoup(response.content, 'html.parser')

    criticas = [critica.text.strip() for critica in critica.find_all('div', {'class': 'review-card-content'})]
    usuarios = [usuario.find_next('div', {'class': 'meta-title'}).text.strip() for usuario in
                critica.find_all('div', {'class': 'review-card-user-infos'})]
    notas = [float(nota.text.replace(',', '.')) for nota in critica.find_all('span', {'class': 'stareval-note'})]
    criticas_usuario = [dict({'usuario': usuarios[i], 'comentario': critica, 'nota:': notas[i]}) for i, critica in
                        enumerate(criticas)]

    serie_dict = {
        'nome': title,
        'sinopse': description,
        'rating': float(rating.replace(',', '.')),
        'generos': genres,
        'atores': atores_personagens,
        'criticas': criticas_usuario,
        'pais': pais,
        'ano': ano,
        'produtores': produtores,
        'duracao': 60
    }

    serie_json = json.dumps(serie_dict)

    print(serie_json)
    return serie_json


## Game of Thrones
# importar_serie('https://www.adorocinema.com/series/serie-7157/', 'temporada-29486/elenco/')
# importar_noticias('https://www.adorocinema.com/series/serie-7157/noticias/', '6450521d43dde1f49d8f110d')

## Breaking Bad
# importar_serie('https://www.adorocinema.com/series/serie-3517/', 'temporada-20885/elenco/')
# importar_noticias('https://www.adorocinema.com/series/serie-3517/noticias/', '645051fc43dde1f49d8f110b')

## This is us
# importar_serie('https://www.adorocinema.com/series/serie-19992/', 'temporada-37176/elenco/')
# importar_noticias('https://www.adorocinema.com/series/serie-19992/noticias/', '6450527143dde1f49d8f110f')

## Grey's anatomy
# importar_serie('https://www.adorocinema.com/series/serie-274/', 'temporada-45971/elenco/')
# importar_noticias('https://www.adorocinema.com/series/serie-274/noticias/', '645052f943dde1f49d8f1111')

## Smallville
# importar_serie('https://www.adorocinema.com/series/serie-62/', 'temporada-16996/elenco/')
# importar_noticias('https://www.adorocinema.com/series/serie-62/noticias/', '6450539a43dde1f49d8f1113')

## Notícias
