from google.oauth2 import service_account
from googleapiclient.discovery import build

# Define the scopes needed
SCOPES = ['https://www.googleapis.com/auth/drive']

# Define your service account credentials
SERVICE_ACCOUNT_FILE = 'path/to/your/service_account_credentials.json'

def download_file_from_drive(file_id, destination_path):
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('drive', 'v3', credentials=creds)

    request = service.files().get_media(fileId=file_id)
    fh = io.FileIO(destination_path, 'wb')
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))

# Example usage
file_id = 'check.txt'
destination_path = './'
download_file_from_drive(file_id, destination_path)