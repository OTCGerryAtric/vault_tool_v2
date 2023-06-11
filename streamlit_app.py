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

response = requests.get('https://www.bungie.net/Platform/Destiny2/PLATFORM/Profile/DESTINY_MEMBERSHIP_ID/',
                            headers=headers)
    if response.status_code == 200:
        st.write(response.json())
    else:
        st.write(f"Request failed with status code {response.status_code}")