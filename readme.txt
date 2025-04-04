Key Changes:
RegexMatchError Handling: Added specific handling for the RegexMatchError that pytube might throw, usually when
the video URL is invalid or the format has changed.

General Exception Handling: This now logs and shows detailed error messages for any other issues encountered
during processing.

Debugging Statements: Added print statements to log the received URL and video title for easier debugging.

Error Rendering: If any errors occur, the error messages are passed to the index.html page to be displayed.

Next Steps:
Make sure you have the latest pytube version: Run the command pip install --upgrade pytube.

Test with different YouTube URLs: Try using different URLs to check if the error persists with all URLs or only
specific ones.