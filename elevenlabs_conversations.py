# /home/ddy/Apps/11labs-call-analysis/elevenlabs_conversations.py
#%%
# /home/ddy/Apps/11labs-call-analysis/elevenlabs_conversations.py
import tkinter as tk
from tkinter import ttk
import pandas as pd
from dotenv import load_dotenv
import os
import elevenlabs_api  # Import the API module
import datetime
import conversation_details

# Load API key from .env file
load_dotenv()
ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

class ElevenLabsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ElevenLabs Conversations")

        # UI elements
        self.fetch_button = ttk.Button(root, text="Fetch Conversations", command=self.fetch_conversations)
        self.fetch_button.pack(pady=10)

        self.tree = ttk.Treeview(root, columns=("agent_id", "conversation_id", "start_time_unix_secs", "call_duration_secs", "agent_name"), show="headings")
        self.tree.heading("agent_id", text="Agent ID")
        self.tree.heading("conversation_id", text="Conversation ID")
        self.tree.heading("start_time_unix_secs", text="Start Time")
        self.tree.heading("call_duration_secs", text="Duration (s)")
        self.tree.heading("agent_name", text="Agent Name")
        self.tree.pack(pady=10)

        # Bind the treeview to the double click event
        self.tree.bind("<Double-1>", self.on_tree_double_click)

    def fetch_conversations(self):
        """Fetches conversations from ElevenLabs API and displays them in the treeview."""
        try:
            conversations_data = elevenlabs_api.get_conversations()  # Use the imported function
            self.populate_treeview(conversations_data)
        except Exception as e:
            print(f"Error fetching conversations: {e}")
            # Display error message in UI (e.g., using a messagebox)

    def populate_treeview(self, conversations_data):
        """Populates the treeview with conversation data."""
        for conversation in conversations_data["conversations"]:
            # Convert Unix timestamp to readable format
            start_time = datetime.datetime.fromtimestamp(conversation.start_time_unix_secs)
            self.tree.insert("", tk.END, values=(
                conversation.agent_id,
                conversation.conversation_id,
                start_time,
                conversation.call_duration_secs,
                conversation.agent_name
            ))

    def on_tree_double_click(self, event):
        """Handles the double click event on the treeview."""
        item = self.tree.selection()[0]  # Get selected item
        conversation_id = self.tree.item(item, "values")[1]  # Get conversation_id from the second column
        details = conversation_details.fetch_conversation_details(conversation_id)
        conversation_details.display_conversation_details(details)

#%%
if __name__ == "__main__":
    root = tk.Tk()
    app = ElevenLabsApp(root)
    root.mainloop()
# %%