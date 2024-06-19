import requests
# client_id, authorize_code 노출 주의, 실제 값은 임시로만 넣고 Git에 올라가지 않도록 유의

client_id = '8dab7975c7ea3d35dc2c471f28ab8909'
redirect_uri = 'https://example.com/oauth'
authorize_code = '3mBYU11qBRwbkrVrJ1sQb5Fpcg6NjqsnPTdfey_g0DdGUrY6SYhHqwAAAAQKKw0fAAABkC3zyn_Nsk3jZ7dWzg'


token_url = 'https://kauth.kakao.com/oauth/token'
data = {
    'grant_type': 'authorization_code',
    'client_id': client_id,
    'redirect_uri': redirect_uri,
    'code': authorize_code,
    }

response = requests.post(token_url, data=data)
tokens = response.json()
print(tokens)