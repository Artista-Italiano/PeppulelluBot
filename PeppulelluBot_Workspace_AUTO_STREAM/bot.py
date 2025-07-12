from dotenv import load_dotenv
import os
import time
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pickle

load_dotenv()

SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]
CLIENT_SECRET_FILE = "client_secret.json"
CREDENTIALS_FILE = "token.pickle"
CHANNEL_ID = os.getenv("CHANNEL_ID")

def get_authenticated_service():
    credentials = None
    if os.path.exists(CREDENTIALS_FILE):
        with open(CREDENTIALS_FILE, "rb") as token:
            credentials = pickle.load(token)
    if not credentials:
        flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
        credentials = flow.run_local_server(port=0)
        with open(CREDENTIALS_FILE, "wb") as token:
            pickle.dump(credentials, token)
    return build("youtube", "v3", credentials=credentials)

def get_live_chat_id(youtube, channel_id):
    request = youtube.liveBroadcasts().list(
        part="snippet",
        broadcastStatus="active",
        broadcastType="all",
        mine=True
    )
    response = request.execute()
    if "items" in response and len(response["items"]) > 0:
        return response["items"][0]["snippet"]["liveChatId"]
    else:
        print("⚠️ Nessuna live attiva trovata.")
        return None

def read_live_chat_messages(youtube, live_chat_id):
    print("📡 Lettura messaggi in tempo reale...")
    request = youtube.liveChatMessages().list(
        liveChatId=live_chat_id,
        part="snippet,authorDetails"
    )
    response = request.execute()
    for item in response.get("items", []):
        author = item["authorDetails"]["displayName"]
        message = item["snippet"]["displayMessage"]
        print(f"💬 {author}: {message}")
        if "ciao" in message.lower():
            send_message(youtube, live_chat_id, f"Ciao {author} 🌞")

def send_message(youtube, live_chat_id, message_text):
    youtube.liveChatMessages().insert(
        part="snippet",
        body={
            "snippet": {
                "liveChatId": live_chat_id,
                "type": "textMessageEvent",
                "textMessageDetails": {
                    "messageText": message_text
                }
            }
        }
    ).execute()

def main():
    print("🤖 PeppulelluBot si sta avviando...")
    youtube = get_authenticated_service()
    chat_id = get_live_chat_id(youtube, CHANNEL_ID)
    if chat_id:
        while True:
            read_live_chat_messages(youtube, chat_id)
            time.sleep(10)

if __name__ == "__main__":
    main()