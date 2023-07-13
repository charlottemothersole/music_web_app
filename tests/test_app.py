# Tests for your routes go here
from lib.album import *
# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===
# def test_get_albums(web_client):
#     response = web_client.get('/albums')
#     assert response.status_code == 200
#     assert response.data.decode("utf-8") == ','.join(['Album(1, My album, 2020, 1)'])

# def test_post_create_album(db_connection, web_client):
#     post_response = web_client.post('/albums', data={
#         'title': 'Voyage', 
#         'release_year': '2022', 
#         'artist_id': '2'
#     })
#     assert post_response.status_code == 200
#     get_response = web_client.get('/albums')
#     assert get_response.status_code == 200
#     assert get_response.data.decode('utf-8') == ','.join(['Album(1, My album, 2020, 1)', 'Album(2, Voyage, 2022, 2)'])

def test_get_artists(db_connection, web_client):
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ','.join([
        'Artist(1, Pixies, Unknown)', 
        'Artist(2, ABBA, Unknown)', 
        'Artist(3, Taylor Swift, Unknown)', 
        'Artist(4, Nina Simone, Unknown)'
    ])

def test_post_create_artist(web_client):
    post_response = web_client.post('/artists', data = {
        'artist': 'Wild nothing', 
        'genre': 'Indie' 
    })
    assert post_response.status_code == 200
    get_response = web_client.get('/artists')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == ','.join([
        'Artist(1, Pixies, Unknown)',
        'Artist(2, ABBA, Unknown)', 
        'Artist(3, Taylor Swift, Unknown)', 
        'Artist(4, Nina Simone, Unknown)', 
        'Artist(5, Wild nothing, Indie)' 
    ])


