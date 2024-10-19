import os
import whisper
# my_secret=os.environ['openaikey']

model=whisper.load_model("base")
result=model.translate("Recording.M4a")
print(result["text"]);

