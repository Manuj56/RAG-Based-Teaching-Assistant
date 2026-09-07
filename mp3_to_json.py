import whisper
import json
import os

model = whisper.load_model("small")

audios = os.listdir("audios/")

for audio in audios:
    # print(audio)
    if("_" in audio):
        number = audio.split("_")[0]
        title = audio.split("_")[1].split(".")[0]
        print(number, title)
        result = model.transcribe(audio = f"audios/{audio}",
                            language = "hi",
                            task = "translate",
                            word_timestamps = False)

        chunks = []
        for segment in result["segments"]:
            chunks.append({"number": number, "title": title, "start": segment["start"], "end": segment["end"], "text": segment["text"]})

        chunks_with_metadata = {"chunks": chunks, "text" : result["text"]}

        filename = audio.replace(".mp3", "")
        with open(f"jsons/{filename}.json", "w") as f:  
            json.dump(chunks_with_metadata, f)
         
