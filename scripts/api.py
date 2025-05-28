import requests

CLIENT_ID = 'cac5c215'

def get_tracks(limit=5):
    url = 'https://api.jamendo.com/v3.0/tracks/'
    params = {
        'client_id': CLIENT_ID,
        'format': 'json',
        'limit': limit,
        'audioformat': 'mp32',
        'include': 'licenses+musicinfo'
    }
    try:
        response = requests.get(url, params=params, timeout=60)
        print('HTTP статус:', response.status_code)
        print('Текст ответа:', response.text[:500])

        response.raise_for_status()
        data = response.json()
        return data.get('results', [])
    except requests.RequestException as e:
        print('Ошибка при запросе:', e)
        return None