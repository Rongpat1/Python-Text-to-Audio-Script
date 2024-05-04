import os
import pyttsx3

def convert_text_to_audio(text_file, output_audio):
    # Check if text file exists
    if not os.path.exists(text_file):
        print("Text file does not exist.")
        return

    # Initialize text-to-speech engine
    engine = pyttsx3.init()

    # Set the audio format to WAV
    engine.setProperty('voice', 'en-us')
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)

    # Open the text file and read the contents
    with open(text_file, 'r') as file:
        text = file.read()

    # Convert the text to audio
    engine.save_to_file(text, output_audio + ".wav")

    # Run the engine to generate the audio
    engine.runAndWait()

if __name__ == "__main__":
    # Specify input text file and output audio file
    text_file = r"input text file name path"
    output_audio = r"output audio file name path"
    convert_text_to_audio(text_file, output_audio)
