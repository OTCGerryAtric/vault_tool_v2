import requests
import webbrowser
import streamlit as st
import requests
import webbrowser

api_key = 'd9194342565e4bf0b8238751543ecb0b'
client_id = '44582'
authorization_url = 'https://www.bungie.net/en/OAuth/Authorize'
url = f"{authorization_url}?client_id={client_id}&response_type=code"

st.markdown(f'[Authorize your Bungie Account]({url})')
webbrowser.open(url)

token_url = 'https://www.bungie.net/platform/app/oauth/token/'
headers = {'X-API-Key': api_key}
data = {
    'grant_type': 'authorization_code',
    'client_id': client_id,
    'code': code,
}

response = requests.post(token_url, headers=headers, data=data)
#
# # The response will contain the access token
# access_token = response.json()['access_token']
#
# st.write(access_token)