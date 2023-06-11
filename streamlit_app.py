import requests
import webbrowser
import streamlit as st

# Setting up Variables
api_key = 'd9194342565e4bf0b8238751543ecb0b'
client_id = '44582'
authorization_url = 'https://www.bungie.net/en/OAuth/Authorize'

# Authorise Bungie Account
url = f"{authorization_url}?client_id={client_id}&response_type=code"
st.markdown(f'[Authorize your Bungie Account]({url})')
webbrowser.open(url)

# Ask the user to enter the authorization code
authorization_code = st.text_input('Please enter the authorization code')
st.write(authorization_code)

# Endpoint for getting the access token
token_url = 'https://www.bungie.net/platform/app/oauth/token/'

# The data to send with the request
data = {'grant_type': 'authorization_code', 'client_id': client_id, 'code': authorization_code}

# Headers for the request
headers = {'X-API-Key': api_key}

# Send the request
response = requests.post(token_url, headers=headers, data=data)

# If the request was successful, print out the returned data
if response.status_code == 200:
    response_data = response.json()
    access_token = response_data['access_token']
    membership_id = response_data['membership_id']
else:
    st.write('Error:', response.status_code)
    st.write('Response:', response.text)

headers = {"Authorization": f"Bearer {access_token}", 'X-API-Key': api_key}
response = requests.get(f'https://www.bungie.net/Platform/User/GetBungieNetUserById/{membership_id}/', headers=headers)

st.write(response)