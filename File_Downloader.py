import os
import io
from googleapiclient.http import MediaIoBaseDownload
from Google import Create_Service

#doesnt work
CLIENT_SECRET_FILE = "sotf-music-updater_client.json"
API_NAME = "drive"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/drive"]

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

file_ids = ["1pzn9mfp7fEE0FE6iIr1pGURKBICwlGgi", "1c6Ozaf6vZymrrLBHKMgBMtP8aDW-Pp_i"]
file_names = ["VHPlains.mp3", "lines.txt"]

for file_id, file_name in zip(file_ids, file_names):
    request = service.files().get_media(fileId=file_id)

    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fd=fh, request=request)

    done = False

    while not done:
        status, done = downloader.next_chunk()
        print(f"Downloading... {0}".format(status.progress() * 100))

    fh.seek(0)

    with open(os.path.join("C:\\Users\\gwynbleidd\\Desktop", file_name), "wb") as f:
        f.write(fh.read())
        f.close()