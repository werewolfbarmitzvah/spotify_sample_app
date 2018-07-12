from pytest import fixture

from spotipy.client import Spotify
from spotipy.oauth2 import SpotifyClientCredentials


@fixture
def mock_spotipy(mocker):
    """
    Test fixture for mocking the spotipy client
    """
    mocker.patch('src.spotify.spotify.create_client')
    creds = SpotifyClientCredentials("clientid", "clientsecret")
    spotipy_client = Spotify(creds)
    spotipy_client.client = mocker.MagicMock()
    spotipy_client.client.return_value = {"access_token": "token",
                                          "token_type": "bearer",
                                          "expires_in": 3600, }
    return spotipy_client
