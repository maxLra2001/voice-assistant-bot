from faster_whisper import WhisperModel

model = WhisperModel("base", device="cpu")

def transcribe(file_path):
    segments, _ = model.transcribe(file_path)
    return " ".join(segment.text for segment in segments)
