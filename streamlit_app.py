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


# import requests
#
# # Your application's details
# api_key = 'd9194342565e4bf0b8238751543ecb0b'
# client_id = '44582'
# authorization_code = 'cec69b531bbd3db31f7f55a4ca4fd258'  # replace with your actual authorization code
#
# # Endpoint for getting the access token
# token_url = 'https://www.bungie.net/platform/app/oauth/token/'
#
# # The data to send with the request
# data = {
#     'grant_type': 'authorization_code',
#     'client_id': client_id,
#     'code': authorization_code,
# }
#
# # The headers for the request
# headers = {
#     'X-API-Key': api_key,
# }
#
# # Send the request
# response = requests.post(token_url, headers=headers, data=data)
#
# # Print the status code and the body of the response
# print(f"Status code: {response.status_code}")
# print(f"Response body: {response.text}")
#
# # If the request was successful, the response will contain the access token
# if response.status_code == 200:
#     response_data = response.json()
#     access_token = response_data['access_token']
#     print(f"Access token: {access_token}")
# else:
#     print("Could not get access token")