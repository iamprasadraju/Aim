from pathlib import Path
from datetime import datetime, timezone
import zoneinfo

import json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# See, edit, share, and permanently delete all the calendars you can access using Google Calendar.
SCOPES = ["https://www.googleapis.com/auth/calendar"]

PROJECT_DIR = Path(__file__).resolve().parents[3]
CONFIG_DIR = PROJECT_DIR / ".config"

CREDENTIALS_FILE = CONFIG_DIR / "gcal_credentials.json"
TOKEN_FILE = CONFIG_DIR / "gcal_token.json"


def oauth_gcal():
    credentials = None

    # if Previously authorized (authorized using token)
    if TOKEN_FILE.is_file():
        credentials = Credentials.from_authorized_user_file(
            TOKEN_FILE,
            SCOPES,
        )

    # No valid authorization yet (redirect to browser)
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            if not CREDENTIALS_FILE.is_file():
                raise FileNotFoundError(
                    f"Credentials file not found: {CREDENTIALS_FILE}"
                )

            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE,
                SCOPES,
            )
            credentials = flow.run_local_server(port=0)

        # writes token to "gcal_token.json"
        TOKEN_FILE.write_text(credentials.to_json())

    return build(
        "calendar",
        "v3",
        credentials=credentials,
    )

def get_today_events():
    service = oauth_gcal()

    now = datetime.now(timezone.utc)
    time_min = datetime.today().replace(hour=0, minute=0, second=0).isoformat() + 'Z'
    time_max = datetime.today().replace(hour=23, minute=59, second=59).isoformat() + 'Z'
    print(time_min, time_max)

    events_result = service.events().list(
        calendarId='primary',
        timeMin=time_min,
        timeMax=time_max,
        singleEvents=True,
        orderBy='startTime'
    ).execute()

    today_events = events_result.get('items', [])

    if not today_events:
        print("no events for today!")
        return

    # print(json.dumps(today_events, indent=4))

    for event in today_events:
        print(event.get("summary"))
    
    
    
if __name__ == "__main__":
    # oauth_gcal()
    get_today_events()
