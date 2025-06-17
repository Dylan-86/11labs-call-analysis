# /home/ddy/Apps/11labs-call-analysis/conversation_details.py
import tkinter as tk
from tkinter import ttk
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

def display_conversation_details(details):
    """Displays conversation details in a new Tkinter window."""
    if not details:
        return

    new_window = tk.Toplevel()
    new_window.title(f"Conversation Details: {details['conversation_id']}")

    # Create a scrolled text widget
    text_area = tk.Text(new_window, wrap=tk.WORD)
    text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    # Insert the details into the text area
    text_area.insert(tk.END, f"Agent ID: {details['agent_id']}\n")
    text_area.insert(tk.END, f"Conversation ID: {details['conversation_id']}\n")
    text_area.insert(tk.END, f"Status: {details['status']}\n")

    # Display phone number from metadata
    if "metadata" in details and "phone_call" in details["metadata"]:
        phone_number = details["metadata"]["phone_call"].get("external_number", "N/A")
        text_area.insert(tk.END, f"Phone Number: {phone_number}\n")
    else:
        text_area.insert(tk.END, "Phone Number: N/A\n")

    text_area.insert(tk.END, "\nTranscript:\n")
    for item in details['transcript']:
        role = item['role']
        message = item['message']
        text_area.insert(tk.END, f"{role}: {message}\n")

    # Disable text area editing
    text_area.config(state=tk.DISABLED)