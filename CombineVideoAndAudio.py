# moviepy needs ffmpeg to be installed on the system
# run 'brew install ffmpeg' to install 

# moviepy also needs the imagemagick library to be installed
# run 'brew install imagemagick' to install imagemagick

# imagemagick also has weord dependencies, so run the following commands to install them

# run 'pip3 install moviepy' to install the moviepy library
from moviepy.editor import *
from moviepy.video.tools.subtitles import SubtitlesClip

def combine_video_and_audio(video_file, audio_file, output_file):
    
    # Load the MP4 video and MP3 audio files
    video_clip = VideoFileClip(video_file)
    audio_clip = AudioFileClip(audio_file)
    
    # Set the audio of the video to the loaded MP3 file
    video_clip = video_clip.set_audio(audio_clip)
    
    # generator for subtitles
    # generator = lambda txt: TextClip(txt, font='Arial', fontsize=35, color='white')
    
    # create subtitles clip
    # subs = SubtitlesClip('synced.srt', generator)
    # subtitles = SubtitlesClip(subs, generator)
    
    # add subtitles to video , subtitles.set_position(('center'))
    video_clip = CompositeVideoClip([video_clip])
    
    # Write the merged video with the audio to a new file
    video_clip.write_videofile(output_file, codec="libx264")
    
    # Close the clips
    video_clip.close()
    audio_clip.close()
    
if __name__ == "__main__":
    # Specify the input video file name
    video_file = "Video.mp4"
    
    # Specify the input audio file name
    audio_file = "TextToSpeechOutput.mp3"
    
    # Specify the output file name
    output_file = "output_video.mp4"
    
    from TTS.api import TTS
    tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2", gpu=True)

    # generate speech by cloning a voice using default settings
    tts.tts_to_file(text="It took me quite a long time to develop a voice, and now that I have it I'm not going to be silent.",
                    file_path="output.wav",
                    speaker_wav=["/path/to/target/speaker.wav"],
                    language="en",
                    split_sentences=True
                    )
    
    # Call the function
    combine_video_and_audio(video_file, audio_file, output_file)