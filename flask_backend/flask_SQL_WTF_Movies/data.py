import requests

def search_movies(title):
    api = 'a00cb754b216bddab6579f83a3140c50'
    params = {'query' : title}
    URL = f'https://api.themoviedb.org/3/search/movie?api_key={api}'
    # title release_date original_title
    data = requests.get(URL, params=params).json()
    data_list = data['results']
    movie_titles = [title['original_title'] for title in data_list]
    release_dates = [date['release_date'] for date in data_list]
    print(len(data['results']))
    print()
    for movie_title, release_date in zip(movie_titles, release_dates):
        if release_date != '':
            select_movies = f'{movie_title} - {release_date}'
            return select_movies