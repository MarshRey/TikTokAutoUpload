# import fuctions from other files
from TextToSpeech import text_to_speech
from CombineVideoAndAudio import combine_video_and_audio
from TextToSrt import text_to_srt

# importing integrated modules
import os

if __name__ == "__main__":
    # get path to text file
    inputtxt = 'text.txt'
    text_file_path = os.path.join(os.path.dirname(__file__), inputtxt)
    
    # parse text file into a format for subtitles
    # Open the input and output files
    text_file_name = "text.txt"
    parced_text_file_name = "parced_text.txt"

    with open(text_file_name, 'r') as input_file, open(parced_text_file_name, 'w') as output_file:
        # Read the content of the input file
        text = input_file.read()

        # Split the text into words
        words = text.split()

        # Write each word followed by a blank line to the output file
        word_count = 0
        for word in words:
            if word_count < 60: # number of words in a video    
                output_file.write(word + '\n\n')
                word_count += 1
            else:
                break
    
    print("Parced_text.txt file created")
    
    # get path to parced text file
    parced_text_file_path = os.path.join(os.path.dirname(__file__), parced_text_file_name)
    
    # convert the text file to a subtitle file
    text_to_srt(parced_text_file_path)

    # Open the file for reading
    with open(text_file_name, 'r') as file:
        # Read the entire content of the file into a single string
        file_content = file.read()

    text = file_content
    
    # generate audio file from text for text to speech
    audio_file = "TextToSpeechOutput.mp3"
    text_to_speech(text, audio_file) # adjusts the audio file
    
    video_file = "MinecraftParkour.mp4" # from youtube
    
    combine_video_and_audio(video_file, audio_file, "output_video.mp4") # combines the audio and video files