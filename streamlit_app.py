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

response = requests.get('https://www.bungie.net/Platform/User/GetMembershipsForCurrentUser/', headers=headers)

if response.status_code == 200:
    response_data = response.json()
    destiny_membership_id = response_data['Response']['destinyMemberships'][0]['membershipId']
    st.write(f"Destiny Membership ID: {destiny_membership_id}")
else:
    st.write(f"Could not get Destiny Membership ID, response status code: {response.status_code}")

# # Send the request
# response = requests.post(token_url, headers=headers, data=data)
#
# # Check if the request was successful
# if response.status_code == 200:
#     response_data = response.json()
#
#     # Print the response_data to debug
#     st.write(response_data)
#
#     # Check if 'membership_id' is in response_data before trying to access it
#     if 'membership_id' in response_data:
#         membership_id = response_data['membership_id']
#         st.write(membership_id)
#     else:
#         st.write("membership_id not found in response data")
# else:
#     st.write(f"Could not get access token, response status code: {response.status_code}")
