# 11Labs Call Analysis

## Description

This project is a simple Flask application that retrieves and displays conversation details from the ElevenLabs API. It allows you to view a list of conversations and their details, including transcripts and metadata.

## Installation

1.  **Clone the repository:**

    ```shell
    git clone <repository_url>
    cd 11labs-call-analysis
    ```

2.  **Create a virtual environment:**

    ```shell
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install the dependencies:**

    ```shell
    pip install -r requirements.txt
    ```

    If you don't have a `requirements.txt` file, create one with the following content:

    ```
    Flask
    requests
    python-dotenv
    elevenlabs
    ```

    And then run `pip install -r requirements.txt`.

4.  **Create a `.env` file:**

    Create a `.env` file in the root directory of the project and add your ElevenLabs API key:

    ```
    ELEVENLABS_API_KEY=<your_elevenlabs_api_key>
    ELEVENLABS_API_URL=https://api.elevenlabs.io/v1/convai/conversations/{conversation_id} # Optional, defaults to this URL
    ```

    Replace `<your_elevenlabs_api_key>` with your actual ElevenLabs API key.

## Usage

1.  **Run the application:**

    ```shell
    python app.py
    ```

2.  **Open the application in your browser:**

    Open your web browser and go to `http://127.0.0.1:5000/` to view the list of conversations.

3.  **View conversation details:**

    Click on a conversation ID to view the details of that conversation, including the transcript and metadata.

## Configuration

The application can be configured using environment variables. The following environment variables are supported:

*   `ELEVENLABS_API_KEY`: Your ElevenLabs API key. This is required.
*   `ELEVENLABS_API_URL`: The URL of the ElevenLabs API. This is optional and defaults to `https://api.elevenlabs.io/v1/convai/conversations/{conversation_id}`.

## License

This project is licensed under the MIT License.