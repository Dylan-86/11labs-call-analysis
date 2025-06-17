import requests
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
API_URL = "https://api.elevenlabs.io/v1/convai/conversations/{conversation_id}"

def fetch_conversation_details(conversation_id, api_key=ELEVENLABS_API_KEY):
    """Fetches conversation details from the ElevenLabs API."""
    try:
        response = requests.get(API_URL.format(conversation_id=conversation_id), headers={"Xi-Api-Key": api_key})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching conversation details: {e}")
        return None

def format_conversations(conversations):
    """Format conversation data including timestamp conversion"""
    formatted = []
    for conv in conversations:
        # Convert Unix timestamp to UTC datetime string
        utc_time = datetime.utcfromtimestamp(conv['start_time_unix_secs']).strftime('%Y-%m-%d %H:%M:%S UTC')
        
        # Create a new conversation object with formatted time
        formatted_conv = conv.copy()
        formatted_conv['start_time_utc'] = utc_time
        formatted.append(formatted_conv)
    
    return formatted