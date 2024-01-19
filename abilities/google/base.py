import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

GOOGLE_SCOPES = [
    'https://www.googleapis.com/auth/calendar.events',
    'https://www.googleapis.com/auth/tasks',
]

def authenticate_with_google():
    try:
        # The file token.json stores the user's access and refresh tokens, and it is
        # created automatically when the authorization flow completes for the first time.
        token_path = 'token.json'

        # If there are no (valid) credentials available, let the user log in.
        creds = None
        if os.path.exists(token_path):
            creds = Credentials.from_authorized_user_file(token_path)
        
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'client_secret.json',
                    GOOGLE_SCOPES,
                )
                creds = flow.run_local_server(port=8035)
            
            # Save the credentials for the next run
            with open(token_path, 'w') as token:
                token.write(creds.to_json())

        return creds
    except Exception:
        return None