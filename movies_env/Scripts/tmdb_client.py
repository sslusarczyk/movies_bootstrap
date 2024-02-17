import requests

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIzYjY2M2M3Y2M3M2MxOTRkYzEzZTU4MWMwYjRiNDI4NCIsInN1YiI6IjY1Y2U3MWE3MDNiZjg0MDE4MWM2MDYxOCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.qQ1xaOv07OocBZEZl88tRiDj3K7vbf40gFMUoFEzw88"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

    
def get_movies(how_many):
    data = get_popular_movies()
    return data["results"][:how_many]
    
popular_movies = get_popular_movies()
print(popular_movies)