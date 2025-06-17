# /home/ddy/Apps/11labs-call-analysis/elevenlabs_api.py
import os
from elevenlabs import ElevenLabs
from dotenv import load_dotenv

load_dotenv()
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

def get_conversations(api_key=ELEVENLABS_API_KEY, page_size=100):
    """Fetches all conversations from the ElevenLabs API, handling pagination."""
    client = ElevenLabs(api_key=api_key)
    conversations = []
    cursor = None

    while True:
        response = client.conversational_ai.conversations.list(page_size=page_size, cursor=cursor)
        conversations.extend(response.conversations)

        if not response.has_more:
            break

        cursor = response.next_cursor

        if cursor is None:
            break

    return { "conversations": conversations }