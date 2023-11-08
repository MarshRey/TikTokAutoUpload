# moviepy needs ffmpeg to be installed on the system
# run 'brew install ffmpeg' to install 

# run 'pip3 install moviepy' to install the moviepy library
from moviepy.editor import *

def combine_video_and_audio(video_file, audio_file, output_file):
    # Load the MP4 video and MP3 audio files
    video_clip = VideoFileClip(video_file)
    audio_clip = AudioFileClip(audio_file)
    
    # Set the audio of the video to the loaded MP3 file
    video_clip = video_clip.set_audio(audio_clip)
    
    # Write the merged video with the audio to a new file
    video_clip.write_videofile(output_file, codec="libx264")
    
    # Close the clips
    video_clip.close()
    audio_clip.close()
    
if __name__ == "__main__":
    # Specify the input video file name
    video_file = "MinecraftParkour.mp4"
    
    # Specify the input audio file name
    audio_file = "TextToSpeechOutput.mp3"
    
    # Specify the output file name
    output_file = "output_video.mp4"
    
    # Call the function
    combine_video_and_audio(video_file, audio_file, output_file)