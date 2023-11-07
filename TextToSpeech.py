# run pip3 install gTTS
from gtts import gTTS

# Input text
text = "Hello, this is your mom who is gay"

# Initialize the gTTS object
tts = gTTS(text)

# Specify the output file name
output_file = "output.mp3"

# Save the speech as an MP3 file
tts.save(output_file)

