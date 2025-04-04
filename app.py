from flask import Flask, request, send_from_directory, url_for, render_template, after_this_request, jsonify
import os
import yt_dlp  # yt-dlp is used to fetch the youtube video files

# Create a Flask web application instance
app = Flask(__name__)

# Defines the folder where downloaded files will be stored
DOWNLOAD_FOLDER = "downloads"
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)  # Create the folder if it doesn't already exist

# Route for the home page (renders index.html)
@app.route('/')
def index():
    return render_template('index.html')

# Route for downloading audio from a provided URL
@app.route('/download', methods=['POST'])
def download():
    # Get the URL from the form data
    url = request.form.get('url')
    if not url:
        return jsonify({"error": "No URL provided"}), 400  # Return an error if no URL is provided

    # yt-dlp options for downloading best audio and converting to mp3
    ydl_opts = {
        'format': 'bestaudio/best',  # Select best audio format
        'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),  # Output file template
        #'cookiefile': '/app/cookies.txt',  # Optional: use cookies for restricted content
        'postprocessors': [{  # Use ffmpeg to extract audio and convert to mp3
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',  # 192 kbps bitrate
        }],
    }
    
    # Download the media using yt-dlp
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)  # Download and get info about the video
        # Prepare the final filename and ensure extension is .mp3
        filename = ydl.prepare_filename(info).replace(".webm", ".mp3").replace(".m4a", ".mp3")
        # Generate a full download URL that points to our server's /serve route
        download_url = url_for('serve_file', filename=os.path.basename(filename), _external=True)
    
    # Return the download URL to the frontend in JSON format
    return jsonify({"download_url": download_url})

# Route for serving the downloaded file to the user
@app.route('/serve/<filename>')
def serve_file(filename):
    file_path = os.path.join(DOWNLOAD_FOLDER, filename)
    
    # If the file does not exist, return 404
    if not os.path.exists(file_path):
        return "File not found", 404
    
    # Use Flask to send the file as an attachment (download prompt in browser)
    response = send_from_directory(DOWNLOAD_FOLDER, filename, as_attachment=True)
    
    # After serving the file, schedule it to be deleted from the server
    @after_this_request
    def remove_file(response):
        try:
            os.remove(file_path)
        except Exception as e:
            print(f"Error deleting file: {e}")
        return response
    
    return response

# Start the Flask app on all available network interfaces (for dev/testing)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)