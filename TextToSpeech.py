# run pip3 install gTTS to install the gTTS library
from gtts import gTTS

def text_to_speech(text, output_file):
    # Initialize the gTTS object
    tts = gTTS(text)
    
    # Save the speech as an MP3 file
    try:
        tts.save(output_file)
        print("File saved successfully")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Input text
    text = "Hello, this is your mom who is gay"

    # Specify the output file name
    output_file = "output.mp3"
    
    # Call the function
    text_to_speech(text, output_file)
