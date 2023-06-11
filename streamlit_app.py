import requests
import webbrowser
import streamlit as st

# Setting up Variables
api_key = 'd9194342565e4bf0b8238751543ecb0b'
client_id = '44582'

# Setting up URL's
base_url = 'https://www.bungie.net/Platform/'
authorization_url = 'https://www.bungie.net/en/OAuth/Authorize'
get_membership_fpr_current_user_url = 'User/GetMembershipsForCurrentUser/'
get_profiles_url = 'Destiny2/{membershipType}/Profile/{destinyMembershipId}/'
get_linked_profiles_url = 'Destiny2/{membershipType}/Profile/{membershipId}/LinkedProfiles/'
get_character_url = 'Destiny2/{membershipType}/Profile/{destinyMembershipId}/Character/{characterId}/'
get_item_url = 'Destiny2/{membershipType}/Profile/{destinyMembershipId}/Item/{itemInstanceId}/'
get_membership_url = 'User/GetMembershipsById/{destinyMembershipId}/1/'

# Authorise Bungie Account
url = f"{authorization_url}?client_id={client_id}&response_type=code"
st.markdown(f'[Authorize your Bungie Account]({url})')
webbrowser.open(url)

# Ask the user to enter the authorization code
authorization_code = st.text_input('Please enter the authorization code')

