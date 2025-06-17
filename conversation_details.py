import requests
import os
from dotenv import load_dotenv

load_dotenv()
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
API_URL = "https://api.elevenlabs.io/v1/convai/conversations/{conversation_id}"

def fetch_conversation_details(conversation_id, api_key=ELEVENLABS_API_KEY):
    """Fetches conversation details from the ElevenLabs API."""
    try:
        response = requests.get(API_URL.format(conversation_id=conversation_id), headers={"Xi-Api-Key": api_key})
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching conversation details: {e}")
        return None