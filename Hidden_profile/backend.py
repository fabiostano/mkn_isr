import base64
import csv
import threading
import time
import os
from flask import Flask, jsonify
from flask_cors import CORS
from vaderSentiment.vaderSentiment import *
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from groq import Groq
from flask import request
from werkzeug.utils import secure_filename
import os

# Initialize Flask app
app = Flask(__name__)

CORS(app)

# Global variables for transcription and summary
full_transcription = ""
current_transcription = ""
overall_summary = ""
processed_files = set()

emotion_counters = {
    'joy': 0,
    'trust': 0,
    'fear': 0,
    'surprise': 0,
    'sadness': 0,
    'disgust': 0,
    'anger': 0,
    'anticipation': 0
}

# Initialize the VADER sentiment analyzer
sentiment_analyzer = SentimentIntensityAnalyzer()

# Groq client initialization
transcription_model = 'whisper-large-v3'
processor_model = 'llama3-8b-8192'
client = Groq(api_key='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')

# Directory to monitor for new audio files
audio_dir = "/home/otree-server-user/hidden_profile_task/audio_dir"


# --- Flask Routes ---
@app.route('/get_summary', methods=['GET'])
def get_summary():
    """Flask route to get the current meeting summary."""
    print(f"Serving summary: {overall_summary}")
    return jsonify({'summary': overall_summary})


@app.route('/get_transcription', methods=['GET'])
def get_transcription():
    """Flask route to get the latest segment of the transcription."""
    global full_transcription
    return jsonify({'transcription': full_transcription})


@app.route('/ask-question', methods=['POST'])
def ask_question():
    """Flask route to handle questions from the user."""
    data = request.get_json()  # Get the JSON data from the request
    user_question = data.get('question')  # Extract the question from the payload

    if not user_question:
        return jsonify({'error': 'No question provided'}), 400  # Handle missing question

    # Call the function to get the AI's response
    ai_answer = answer_transcription_content_questions(user_question)

    # Return the response as JSON
    return jsonify({'answer': ai_answer})


@app.route('/upload_recording', methods=['POST'])
def upload_recording():
    try:
        if 'audio' not in request.files:
            return jsonify({'error': 'No audio file provided'}), 400
            
        audio_file = request.files['audio']
        if audio_file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
            
        filename = secure_filename(audio_file.filename)
        filepath = os.path.join(audio_dir, filename)
        
        audio_file.save(filepath)
        
        # Process the file immediately
        process_new_file(filepath)
        
        return jsonify({
            'message': 'Recording uploaded and processed',
            'filename': filename
        }), 200
        
    except Exception as e:
        print(f"Error handling recording upload: {e}")
        return jsonify({'error': str(e)}), 500
    


@app.route('/get_vader_compound', methods=['GET'])
def get_vader_compound():
    """Flask route to get the compound score for each transcription."""
    print("serving vader compound")
    global current_transcription
    if not current_transcription:
        return jsonify({'compound': 0})  # Handle cases with no transcription
    sentiment = sentiment_analyzer.polarity_scores(current_transcription)
    compound_score = sentiment['compound']
    print(compound_score)
    return jsonify({'compound': compound_score})


@app.route('/get_meeting_compound', methods=['GET'])
def get_meeting_compound():
    """Flask route to get the compound score for the entire meeting transcription."""
    print("serving meeting compound")
    global full_transcription
    if not full_transcription:
        return jsonify({'compound': 0})  # Handle case with no transcription

    sentiment = sentiment_analyzer.polarity_scores(full_transcription)
    compound_score = sentiment['compound']
    print(compound_score)
    return jsonify({'compound': compound_score})


@app.route('/cleanup_recordings', methods=['POST'])
def cleanup_recordings():
    """Endpoint to delete all audio recordings once the meeting ends."""
    try:
        for filename in os.listdir(audio_dir):
            file_path = os.path.join(audio_dir, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
                print(f"Deleted file: {file_path}")
        return jsonify({'message': 'All recordings deleted successfully.'}), 200
    except Exception as e:
        print(f"Error during cleanup: {e}")
        return jsonify({'message': 'Error during cleanup.', 'error': str(e)}), 500


# --- Groq-Based Functions ---

def audio_to_text(filepath):
    """Convert audio file to text using Groq's Whisper model."""
    with open(filepath, "rb") as file:
        translation = client.audio.translations.create(
            file=(filepath, file.read()),
            model=transcription_model,
        )
    return translation.text


def summarize_transcription(transcription):
    """Generate summary of the transcription using Groq's model."""
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": f"You are an AI assistant tasked with summarizing the content from "
                               f"the following transcription: {transcription}. "
                               f"As an output, give only the summary."
                }
            ],
            model=processor_model,
        )
        summary = chat_completion.choices[0].message.content
        print(f"Generated summary: {summary}")
        return summary
    except Exception as e:
        print(f"Error during summarization: {e}")
        return "Error in summarization"


def answer_transcription_content_questions(user_question):
    """Answer user questions about the meeting content."""
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": f"Use the transcription {full_transcription} to answer the question: "
                           f"{user_question}. Provide the most accurate response."
            }
        ],
        model=processor_model,
    )
    return chat_completion.choices[0].message.content


# ----------- CSV File with the sentiment scores for the analysis ------------------
# Path to the CSV file
CSV_FILE = "/home/otree-server-user/hidden_profile_task/sentiment_scores.csv"
# Directory to store the images
IMAGE_SAVE_DIRECTORY = '/home/otree-server-user/hidden_profile_task/chart_images'
# Ensure the directory exists
os.makedirs(IMAGE_SAVE_DIRECTORY, exist_ok=True)

# Initialize the CSV file if it doesn't exist
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "sentiment_compound"])  # Write the header


@app.route('/save_sentiment', methods=['POST'])
def save_sentiment():
    try:
        # Get data from the POST request
        data = request.json
        timestamp = data.get("timestamp")
        sentiment_compound = data.get("sentiment_compound")

        if not timestamp or sentiment_compound is None:
            return jsonify({"error": "Invalid data"}), 400

        # Append the data to the CSV file
        with open(CSV_FILE, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([timestamp, sentiment_compound])

        return jsonify({"message": "Sentiment data saved successfully"}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/store_chart_image', methods=['POST'])
def store_chart_image():
    try:
        data = request.json
        image_data = data['image']
        timestamp = data.get('timestamp', 'unknown')

        # Decode the Base64 image
        header, encoded = image_data.split(',', 1)  # Separate metadata and image data
        image_binary = base64.b64decode(encoded)

        # Create a filename with timestamp
        filename = f"sentiment_chart_{timestamp.replace(':', '-').replace(' ', '_')}.png"
        filepath = os.path.join(IMAGE_SAVE_DIRECTORY, filename)

        # Save the image
        with open(filepath, 'wb') as f:
            f.write(image_binary)

        return jsonify({'message': 'Chart image stored successfully!', 'filepath': filepath}), 200
    except Exception as e:
        print(f"Error saving chart image: {e}")
        return jsonify({'error': str(e)}), 500


# ------------- Save a word count for the transcriptions --------------
# Path to the CSV file
WORD_COUNT_CSV_FILE = "/home/otree-server-user/hidden_profile_task/words_spoken.csv"

# Ensure the CSV file is initialized
if not os.path.exists(WORD_COUNT_CSV_FILE):
    with open(WORD_COUNT_CSV_FILE, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['timestamp', 'word_count'])  # Add headers



@app.route('/get_word_count', methods=['GET'])
def get_word_count():
    """Get accurate word count from the full transcription."""
    global full_transcription
    
    if not full_transcription:
        return jsonify({'word_count': 0})
        
    # Clean and count words
    words = full_transcription.lower()
    # Remove punctuation and special characters
    words = re.sub(r'[^\w\s]', ' ', words)
    # Split on whitespace and filter empty strings
    word_list = [w for w in words.split() if w]
    
    return jsonify({'word_count': len(word_list)})



@app.route('/store_word_count', methods=['POST'])
def store_word_count():
    """Store the word count in a CSV file."""
    data = request.get_json()
    word_count = data.get('word_count')
    timestamp = data.get('timestamp')

    if word_count is None or timestamp is None:
        return jsonify({'message': 'Invalid data received'}), 400

    # Append the word count to the CSV file
    try:
        with open(WORD_COUNT_CSV_FILE, mode='a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([timestamp, word_count])
        return jsonify({'message': 'Word count stored successfully'}), 200
    except Exception as e:
        print(f"Error writing to CSV: {e}")
        return jsonify({'message': 'Failed to store word count', 'error': str(e)}), 500


# --- Audio File Processing ---
class AudioHandler(FileSystemEventHandler):
    """Watchdog event handler to monitor new audio files."""

    def on_created(self, event):
        """Called when a new file is created in the monitored directory."""
        if event.is_directory:
            return
        if event.src_path.endswith((".mp3", ".wav", ".webm")):
            process_new_file(event.src_path)


def process_new_file(filepath):
    """Process new audio files, transcribe, and update the overall summary."""
    global full_transcription, overall_summary, current_transcription
    try:
        if filepath not in processed_files:  # Only process unprocessed files
            print(f"Processing {os.path.basename(filepath)}...")
            try:
                current_transcription = audio_to_text(filepath)
                if current_transcription:
                    full_transcription += current_transcription + " "
                    print(f"Updated Full Transcription: {full_transcription}")
                    # Generate and update the summary
                    overall_summary = summarize_transcription(full_transcription)
                    print(f"Updated Overall Summary: {overall_summary}")
                processed_files.add(filepath)
            except Exception as e:
                print(f"Error in transcription/summary generation: {e}")
    except Exception as e:
        print(f"Error processing {os.path.basename(filepath)}: {e}")


# --- Running Flask and Audio Processing Concurrently ---

def run_flask():
    """Run Flask server on a separate thread."""
    app.run(debug=False, use_reloader=False)


def monitor_audio_directory():
    """Start monitoring the audio directory for new files."""
    event_handler = AudioHandler()
    observer = Observer()
    observer.schedule(event_handler, path=audio_dir, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)  # Keep the observer running
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
    # Start Flask server in a separate thread
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    # Start monitoring the audio directory in a separate thread
    monitor_thread = threading.Thread(target=monitor_audio_directory)
    monitor_thread.daemon = True
    monitor_thread.start()
