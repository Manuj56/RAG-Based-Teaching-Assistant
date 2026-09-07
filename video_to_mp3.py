#convert the videos to mp3
import os
import subprocess

files = os.listdir("Videos")
for file in files:
    tutorial_name = file.split("_")[0]
    file_name = file.split("_")[1].split(".mp4")[0]
    print(tutorial_name, file_name)
    subprocess.run(["ffmpeg", "-i", f"Videos/{file}", f"audios/{tutorial_name}_{file_name}.mp3"])