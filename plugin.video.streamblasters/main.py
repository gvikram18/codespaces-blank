import xbmcgui
import xbmcplugin
import requests
from bs4 import BeautifulSoup

torrent_site_url = "https://streamblasters.co/"

def search_movies(query):
    url = f"{torrent_site_url}/search/{query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    results = soup.find_all('div', {'class': 'movie-result'})
    movies = []
    for result in results:
        title = result.find('h3').text
        torrent_link = result.find('a', {'class': 'torrent-link'})['href']
        movies.append((title, torrent_link))
    return movies
    

def play_movie(torrent_link):
    # TODO: Write this function
    pass

def search_movies_and_display_results():
    # TODO: Write this function
    pass