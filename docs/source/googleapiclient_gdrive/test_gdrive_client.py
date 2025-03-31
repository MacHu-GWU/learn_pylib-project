# -*- coding: utf-8 -*-

import json
from pathlib import Path

import google.auth.exceptions
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/drive"]

dir_here = Path(__file__).absolute().parent
path_temp_json = dir_here / "tmp.json"

dir_home = Path.home()
dir_google = dir_home / ".google"
dir_google.mkdir(parents=True, exist_ok=True)

path_client_secrets = (
    dir_google / "read_and_write_files_via_google_drive_api_poc_client_secrets.json"
)
# If modifying these scopes, delete the file send_and_receive_email_via_gmail_poc_token.json.
path_token = (
    dir_google / "read_and_write_files_via_google_drive_api_poc_client_token.json"
)


def auth():
    """Shows basic usage of the Drive v3 API.
    Prints the names and ids of the first 10 files the user has access to.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if path_token.exists():
        creds = Credentials.from_authorized_user_file(str(path_token), SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        need_re_auth = True
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
                need_re_auth = False
            except google.auth.exceptions.RefreshError as e:
                pass

        if need_re_auth:
            flow = InstalledAppFlow.from_client_secrets_file(
                str(path_client_secrets),
                SCOPES,
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        path_token.write_text(creds.to_json())

    service = build("drive", "v3", credentials=creds)
    return service


def list_files(service):
    # Call the Drive v3 API
    results = (
        service.files()
        # fmt: off
        .list(
            # q="mimeType='application/vnd.google-apps.folder'", # Folder only
            # q="mimeType='application/vnd.google-apps.folder' and 'root' in parents and trashed=false", # Folder in Root Folder
            q="mimeType='application/vnd.google-apps.document' and trashed=false", # Google Doc only
            pageSize=50,
            # fields="nextPageToken, files(id, name, mimeType, size, parents, webViewLink)",
            fields="nextPageToken, files(*)",
        )
        # fmt: on
        .execute()
    )
    items = results.get("files", [])
    for item in items:
        print(f"{item = }")


def download_google_doc(service):
    file_id = "1FZk9SY6UXdiqkOPmFAqcRdYd2kTl3kniEXn8VT5mZeI"

    # Define export format (Choose one)
    export_mime_type = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"  # DOCX format
    # export_mime_type = "application/pdf"  # PDF format
    # export_mime_type = "text/plain"  # TXT format

    # Request to export the file
    request = service.files().export_media(fileId=file_id, mimeType=export_mime_type)
    file_data = request.execute()

    # Save to local file
    output_filename = "downloaded_document.docx"  # Change as needed
    with open(output_filename, "wb") as f:
        f.write(file_data)


if __name__ == "__main__":
    service = auth()
    list_files(service)
    # download_google_doc(service)
