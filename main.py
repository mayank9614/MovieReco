from flask import Flask, request, jsonify
import requests
import base64

app = Flask(__name__)

CLIENT_ID = 'hidden'
CLIENT_SECRET = 'hidden'

SPOTIFY_TOKEN_URL = 'https://accounts.spotify.com/api/token'
SPOTIFY_SEARCH_URL = 'https://api.spotify.com/v1/search'

def get_spotify_token():
    client_credentials = f"{CLIENT_ID}:{CLIENT_SECRET}"
    headers = {
        "Authorization": "Basic " + base64.b64encode(client_credentials.encode()).decode('utf-8')
    }
    payload = {
        'grant_type': 'client_credentials'
    }
    response = requests.post(SPOTIFY_TOKEN_URL, data=payload, headers=headers)
    return response.json().get('access_token')

@app.route('/search_playlist', methods=['GET'])
def search_playlist():
    movie_name = request.args.get('movie_name')
    token = get_spotify_token()
    headers = {
        "Authorization": f"Bearer {token}"
    }
    params = {
        'q': movie_name,
        'type': 'playlist',
        'limit': 10
    }
    response = requests.get(SPOTIFY_SEARCH_URL, headers=headers, params=params)
    playlists = response.json().get('playlists', {}).get('items', [])
    return jsonify(playlists)

if __name__ == '__main__':
    app.run(debug=True)
