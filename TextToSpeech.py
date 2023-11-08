# run pip3 install gTTS to install the gTTS library
from gtts import gTTS

def text_to_speech(text, output_file):
    # Initialize the gTTS object
    tts = gTTS(text)
    
    # Save the speech as an MP3 file
    try:
        tts.save(output_file)
        print("TextToSpeechOutput.mp3 file created")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Input text
    text = "Wow!, this minecraft parkour is so hard! But i know with hard work and dedication, i can do it!"

    # Specify the output file name
    output_file = "TextToSpeechOutput.mp3"
    
    # Call the function
    text_to_speech(text, output_file)
