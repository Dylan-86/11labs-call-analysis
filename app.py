from flask import Flask, render_template, jsonify
import elevenlabs_api
import conversation_details

app = Flask(__name__)

@app.route("/")
def index():
    """Renders the main page with the list of conversations."""
    conversations = elevenlabs_api.get_conversations()
    return render_template("index.html", conversations=conversations["conversations"])

@app.route("/conversation/<conversation_id>")
def conversation_details_route(conversation_id):
    """Returns the details of a specific conversation as JSON."""
    details = conversation_details.fetch_conversation_details(conversation_id)
    return render_template("conversation_details.html", details=details)

if __name__ == "__main__":
    app.run(debug=True)