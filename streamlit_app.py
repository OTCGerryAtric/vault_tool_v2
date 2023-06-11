import requests
import webbrowser
import streamlit as st

import requests
import webbrowser

# Your application's details
api_key = 'd9194342565e4bf0b8238751543ecb0b'
client_id = '44582'
authorization_url = 'https://www.bungie.net/en/OAuth/Authorize'

# Construct the URL the user needs to go to grant access to your application
url = f"{authorization_url}?client_id={client_id}&response_type=code"

# Open the authorization URL in the user's web browser
webbrowser.open(url)

# The user will now see the Bungie login page and will need to grant your application access.
# After they do, they'll be redirected to your redirect URI, with a "code" query parameter added by Bungie.
# You'll need to extract this code from the URL.
# For the sake of this example, we'll assume you've done this and saved the code in a variable:
code = "THE_CODE_FROM_THE_REDIRECT_URI"

# Now that you have the code, you can exchange it for an access token.
token_url = 'https://www.bungie.net/platform/app/oauth/token/'
headers = {'X-API-Key': api_key}
data = {
    'grant_type': 'authorization_code',
    'client_id': client_id,
    'code': code,
}

response = requests.post(token_url, headers=headers, data=data)

# The response will contain the access token
access_token = response.json()['access_token']

st.write(access_token)