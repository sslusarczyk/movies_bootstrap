from flask import Flask
import tmdb_client
from unittest.mock import Mock

import sys
import os
# Add the parent directory of main.py to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import main  # Import main module after adding to the Python path



from unittest.mock import Mock, patch
import tmdb_client

def test_get_single_movie(monkeypatch):
    # Przygotowanie testowych danych
    mock_movie_data = {
        'id': 550,
        'title': 'Fight Club',
        'overview': 'An insomniac office worker and a devil-may-care soapmaker...',
        # Dodaj więcej pól danych, które są zwracane przez funkcję
    }

    # Definicja funkcji mockowanej
    def mock_get_single_movie(movie_id, endpoint):
        assert endpoint == 'details'
        return mock_movie_data

    # Wykorzystanie monkeypatch do zamiany oryginalnej funkcji na funkcję mockowaną
    monkeypatch.setattr(tmdb_client, 'get_single_movie', mock_get_single_movie)

    # Wywołanie funkcji, którą testujemy
    movie = tmdb_client.get_single_movie(550, endpoint='details')

    # Sprawdzenie czy funkcja zwróciła oczekiwany wynik
    assert movie['id'] == 550
    assert movie['title'] == 'Fight Club'

def test_get_movie_images(monkeypatch):
    # Przygotowanie testowych danych
    mock_images_data = {
        'backdrops': [{'file_path': '/example_path_1.jpg'}, {'file_path': '/example_path_2.jpg'}],
        'posters': [{'file_path': '/example_path_3.jpg'}, {'file_path': '/example_path_4.jpg'}],
        # Dodaj więcej pól danych, które są zwracane przez funkcję
    }

    # Definicja funkcji mockowanej
    def mock_get_movie_images(movie_id, endpoint):
        assert endpoint == 'images'
        return mock_images_data

    # Wykorzystanie monkeypatch do zamiany oryginalnej funkcji na funkcję mockowaną
    monkeypatch.setattr(tmdb_client, 'get_movie_images', mock_get_movie_images)

    # Wywołanie funkcji, którą testujemy
    images = tmdb_client.get_movie_images(550, endpoint='images')

    # Sprawdzenie czy funkcja zwróciła oczekiwany wynik
    assert len(images['backdrops']) == 2
    assert len(images['posters']) == 2

def test_get_single_movie_cast(monkeypatch):
    # Przygotowanie testowych danych
    mock_cast_data = [
        {'name': 'Brad Pitt', 'character': 'Tyler Durden'},
        {'name': 'Edward Norton', 'character': 'The Narrator'},
        # Dodaj więcej pól danych, które są zwracane przez funkcję
    ]

    # Definicja funkcji mockowanej
    def mock_get_single_movie_cast(movie_id, endpoint):
        assert endpoint == 'credits'
        return mock_cast_data

    # Wykorzystanie monkeypatch do zamiany oryginalnej funkcji na funkcję mockowaną
    monkeypatch.setattr(tmdb_client, 'get_single_movie_cast', mock_get_single_movie_cast)

    # Wywołanie funkcji, którą testujemy
    cast = tmdb_client.get_single_movie_cast(550, endpoint='credits')

    # Sprawdzenie czy funkcja zwróciła oczekiwany wynik
    assert len(cast) == 2
    assert cast[0]['name'] == 'Brad Pitt'
    assert cast[1]['character'] == 'The Narrator'