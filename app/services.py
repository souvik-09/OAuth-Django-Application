import requests

client_id = 'oauth provider client id goes here'
client_secret = 'oauth provider client secret goes here'
token_url = 'https://xxxxxxxxxxx/nidp/oauth/nam/token'
redirect_uri = 'http://xxxxxxxxxxx/callback'
authorization_base_url = 'https://xxxxxxxxxxx/nidp/oauth/nam/authz'
user_info_url = 'https://xxxxxxxxxxx/nidp/oauth/nam/userinfo'
logout_base_url = 'https://xxxxxxxxxxx/nidp/oauth/v1/nam/end_session'
token_info_url = 'https://xxxxxxxxxxx/nidp/oauth/nam/tokeninfo'

def get_oauth_token_info(token):
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.get(token_info_url, headers=headers, verify=False)

    # Check if the request was successful
    if response.status_code == 200:
        return response.json()  # Return the token information as a dictionary
    else:
        # Handle errors (e.g., invalid token, expired token)
        return {"error": f"Failed to retrieve token information, status code: {response.status_code}"} 

        