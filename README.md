# OAuth Django Integration

A Django application that implements OAuth 2.0 authentication using an external OAuth provider (Access Manager).

## Project Structure

```
oauth_django/
├── app/                    # Main application directory
│   ├── services.py        # OAuth service functions
│   ├── urls.py            # Application URL routing
│   ├── views.py           # View handlers
│   └── ...
├── oauth_app/             # Project configuration
│   ├── settings.py        # Django settings
│   ├── urls.py            # Project URL routing
│   └── ...
├── manage.py              # Django management script
├── requirements.txt       # Project dependencies
└── db.sqlite3             # SQLite database
```

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Installation

1. Clone the repository
2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies using requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Before running the application, you need to configure the OAuth settings in `app/services.py`:

```python
client_id = 'your_client_id'
client_secret = 'your_client_secret'
token_url = 'your_token_url'
redirect_uri = 'your_redirect_uri'
authorization_base_url = 'your_authorization_url'
user_info_url = 'your_user_info_url'
logout_base_url = 'your_logout_url'
token_info_url = 'your_token_info_url'
```

## Running the Application

1. Start the Django development server:
   ```bash
   python manage.py runserver
   ```

2. Access the application at `http://localhost:8000`

## Features

- OAuth 2.0 authentication flow
- User login and logout functionality
- Session management
- Token validation and user information retrieval

## Authentication Flow

1. User visits the application
2. Clicks on login link
3. Redirected to OAuth provider's login page
4. After successful authentication, redirected back to application
5. Application exchanges authorization code for access token
6. User information is retrieved and stored in session
7. User can logout, which clears the session and redirects to OAuth provider's logout page

## Security Notes

- The application uses session-based authentication
- Access tokens are stored in the session
- SSL verification is disabled for development purposes (verify=False)
- In production, proper SSL verification should be enabled

## Troubleshooting

If you encounter issues:
1. Check the OAuth configuration in `services.py`
2. Verify that the redirect URI is correctly configured in your OAuth provider
3. Ensure all required URLs are accessible
4. Check the Django server logs for error messages
