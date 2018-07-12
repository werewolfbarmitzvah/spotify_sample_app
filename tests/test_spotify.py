from mock import patch
from spotipy.client import Spotify

from src.spotify import spotify


def test_spotipy_credentials_manager(mock_spotipy):
    assert mock_spotipy._auth.client_id == 'clientid'
    assert mock_spotipy._auth.client_secret == 'clientsecret'


def test_spotipy_client_auth(mock_spotipy):
    assert mock_spotipy.client.return_value == {"access_token": "token",
                                                "token_type": "bearer",
                                                "expires_in": 3600, }


def test_spotipy_client_instance(mock_spotipy):
    assert isinstance(mock_spotipy, Spotify)


@patch.object(spotify, 'is_related')
def test_is_relation_called(mock):
    spotify.is_related("Jawbreaker", "Cursive")
    mock.assert_called_with("Jawbreaker", "Cursive")
