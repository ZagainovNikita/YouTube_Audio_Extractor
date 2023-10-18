from pytube import YouTube
from moviepy.editor import VideoFileClip
import os

class Extractor:
    def __init__(self, youtube_link: str):
        self.link = youtube_link

    def download_video(self, output_filename: str = "video.mp4"):
        try:
            (YouTube(self.link)
             .streams
             .first()
             .download(output_path='downloads', filename=output_filename))
        except:
            raise Exception("video not found")

    def extract_audio(self, output_filename: str = "audio.mp3"):
        try:
            self.download_video(),
            video_clip = VideoFileClip("downloads//video.mp4")
            audio = video_clip.audio
            output_filepath = os.path.join("extracted", output_filename)
            audio.write_audiofile(output_filepath)
            audio.close()
            video_clip.close()
        except:
            raise Exception(f"wrong filepath")