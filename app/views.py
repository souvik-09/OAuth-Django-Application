from django.http import HttpResponse
from django.shortcuts import redirect
from app.services import *


def index(request):
    if 'access_token' in request.session:
        return redirect('success')
    return HttpResponse('You are not logged in. <a href="/login">Login</a>')

def login(request):
    # Redirect the user to Access Manager's login page
    authorization_url = f"{authorization_base_url}?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}"
    return redirect(authorization_url)

def callback(request):
    code = request.GET.get('code')
    if not code:
        return HttpResponse('Authorization failed. Authorization code not provided.')

    try:
        # Exchange the authorization code for an access token
        token_response = requests.post(token_url, data={
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': redirect_uri,
            'client_id': client_id,
            'client_secret': client_secret,
        }, verify=False)

        print("Token Response Status Code:", token_response.status_code)
        print("Token Response Content:", token_response.text)

        if token_response.status_code == 200:
            try:
                access_token = token_response.json().get('access_token')
                if not access_token:
                    print("Access token not found in response.")
                    return HttpResponse('Access token not found in response.')

                # Save access token to session
                request.session['access_token'] = access_token

                # Retrieve user info using the access token
                user_info = get_oauth_token_info(access_token)
                print("User Info:", user_info)

                request.session['username'] = user_info.get('user_id')
                return redirect('success')
            except Exception as e:
                print("Exception while processing access token:", e)
                return HttpResponse('An error occurred while processing the access token.')
        else:
            return HttpResponse(f"Failed to retrieve access token. Status Code: {token_response.status_code}, Error: {token_response.text}")
    except Exception as err:
        print("Exception occurred:", err)
        return HttpResponse('An unexpected error occurred.')

def success(request):
    if 'username' not in request.session:
        return redirect('index')

    username = request.session.get('username')
    return HttpResponse(f"Success! You are now authorized as: {username} <br> <br> <a href='/logout'>Logout</a>")

def logout(request):
    # Clear session and redirect to logout URL
    request.session.flush()
    oauth_logout_url = f"{logout_base_url}?client_id={client_id}&logout_uri={redirect_uri}"
    return redirect(oauth_logout_url)