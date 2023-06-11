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

# Ask the user to enter the access token
access_token = st.text_input('Please enter your access token')
st.write(access_token)


# Endpoint for getting the access token
token_url = 'https://www.bungie.net/platform/app/oauth/token/'

# The data to send with the request
data = {
    'grant_type': 'authorization_code',
    'client_id': client_id,
    'code': access_token,
}

# The headers for the request
headers = {
    'X-API-Key': api_key,
}

# Send the request
response = requests.post(token_url, headers=headers, data=data)
response_data = response.json()
membership_id = response_data['membership_id']
print(membership_id)  # This will print '9354468'