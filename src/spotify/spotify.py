import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from src.settings import CLIENT_ID, CLIENT_SECRET


def create_client():
    """
    Return a Spotify client using the client credentials authentication flow
    """
    client_credentials_manager = SpotifyClientCredentials(
        client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    return spotipy.Spotify(
        client_credentials_manager=client_credentials_manager)


def is_related(artist, compared_artist):
    """
    Checks to see if there is a relation
    """
    first_artist_id = _search_artist(artist)
    compared_artist_id = _search_artist(compared_artist)
    related_artists = _get_related_artists(compared_artist_id)
    for artists in related_artists['artists']:
        if artists['id'] == first_artist_id:
            return True
        else:
            continue


def _get_related_artists(artist_id):
    """
    Helper method to get the related artists
    """
    return create_client().artist_related_artists(artist_id)


def _search_artist(artist_name):
    """
    Helper method to search for an artist. Only gets the first one
    """
    return create_client().search(artist_name, limit=1,
                                  type='artist')['artists']['items'][0]['id']
