# import fuctions from other files
from TextToSpeech import text_to_speech
from CombineVideoAndAudio import combine_video_and_audio

if __name__ == "__main__":
    text = "Large Cock"
    audio_file = "TextToSpeechOutput.mp3"
    text_to_speech(text, audio_file) # adjusts the audio file
    
    video_file = "MinecraftParkour.mp4" # from youtube
    
    combine_video_and_audio(video_file, audio_file, "output_video.mp4") # combines the audio and video files