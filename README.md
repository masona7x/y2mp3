A simple and fast YouTube to MP3 converter app built with yt-dlp and Flask. Easily convert YouTube videos to high-quality MP3 files with one click



🚀 Features

-Convert YouTube videos to MP3 format quickly.

-High-quality audio output (up to 320kbps).

-Built with yt-dlp (a powerful video downloader).

-User-friendly interface 



⚡ How It Works

-Paste the YouTube video URL into the app.

-Click the convert button to start downloading.

-Download the MP3 file once the conversion is complete.



📦 Requirements

-OPTIONAL - There is a Dockerfile included in the root of the project folder if you would like to containerize this app, see install instructions below

-Python 3.x must be installed on your system.

-Required Dependecies:

 -Flask==3.1.0
 -pip==23.0.1
 -pipreqs==0.5.0
 -setuptools==65.5.0
 -tinycss2==1.4.0
 -youtube-dl==2021.12.17
 -yt-dlp==2025.3.27

-To properly install all dependicies, use the requirements.txt file in the root of the project folder

-Use command pip install -r requirements.txt while in the root of the project folder




🛠 Installation

-Clone this repository from GitHub.

-In your terminal, navigate to the project folder.

-Install the required Python packages using pip.

-Run the python app.py command to start the Flask server.

-Open your web browser and go to http://127.0.0.1:5000 or http://localhost:5000


DOCKER INSTALL STEPS

-Make sure you have docker installed 

-Navigate to the root of the project folder in your terminal

-To build the image, run "docker build -t y2mp3 ."

-Now that you have your y2mp3 image you can run the image in a container

-To run the image, with port 5000 exposed, run command "docker run -d -p 5000:5000 --name y2mp3 y2mp3"



💻 Usage

-Launch the application.

-Open your web browser and go to http://127.0.0.1:5000 or http://localhost:5000

-Paste any YouTube video URL into the input field.

-Click Convert to start the download.

-Once the conversion is complete, click Download to save the MP3.



🧑‍💻 Contributing

-Contributions are welcome! If you'd like to contribute, please fork this repository and submit a pull request with your changes.

📄 License

-TBD

📝 Acknowledgements

-yt-dlp for video downloading and conversion and Flask for the web framework.

