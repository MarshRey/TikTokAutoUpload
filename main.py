# import fuctions from other files
from TextToSpeech import text_to_speech
from CombineVideoAndAudio import combine_video_and_audio
from TextToSrt import text_to_srt

# importing integrated modules
import os

# ffs video.mp4 -i unsynchronized.srt -o synchronized.srt
# https://pypi.org/project/ffsubsync/




if __name__ == "__main__":
    
    # word replacemnet disctionary
    word_replacements = {
        "AITA": "Am I the Asshole",
        "SIL": "Sister-in-law",
    }
    
    # get path to text file
    inputtxt = 'text.txt'
    text_file_path = os.path.join(os.path.dirname(__file__), inputtxt)
    
    # parse text file into a format for subtitles
    # Open the input and output files
    text_file_name = "text.txt"
    parced_text_file_name = "parced_text_for_srt.txt"
        
    with open(text_file_name, 'r') as input_file, open(parced_text_file_name, 'w') as output_file, open("edited_text_file_for_tts.txt", 'w') as output_tts_file:
        # Read the content of the input file
        text = input_file.read()

        # Split the text into words
        words = text.split()

        # Write each word followed by a blank line to the output file
        word_count = 0
        for word in words:
            # make srt text file
            if word_count < 100: # number of words wanted in a video    
                output_file.write(word + '\n\n')
                word_count += 1
            else:
                break
            
            # make text file for tts using word replacements from the dictionary
            if word in word_replacements:
                output_tts_file.write(word_replacements[word] + ' ')
            else:
                output_tts_file.write(word + ' ')
            
    print("Parced_text_for_srt.txt and edited_text_file_for_tts.txt created")
    
    # get path to parced text file
    parced_text_file_path = os.path.join(os.path.dirname(__file__), parced_text_file_name)
    
    # convert the text file to a subtitle file
    text_to_srt(parced_text_file_path)

    # Open the file for reading
    with open("edited_text_file_for_tts.txt", 'r') as file:
        # Read the entire content of the file into a single string
        file_content = file.read()

    text = file_content

    # Specify the output file name
    output_file = "TextToSpeechTestOutput.mp3"
    
    # Call the function
    text_to_speech(text, output_file)
    
    video_file = "MinecraftParkour.mp4" # from youtube
    
    combine_video_and_audio(video_file, output_file, "output_video.mp4") # combines the audio and video files