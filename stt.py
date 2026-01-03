import sounddevice as sd
import numpy as np
import whisper

# Load Whisper model (offline)
model = whisper.load_model("small")  # "base", "small", "medium" all work

def record_audio(duration=5, fs=16000):
    """Record audio from microphone"""
    print("Recording...")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype="float32")
    sd.wait()
    print("Done recording.")
    return audio.flatten()

def speech_to_text(audio):
    """Convert audio to text using Whisper"""
    audio = np.array(audio, dtype=np.float32)
    result = model.transcribe(audio, fp16=False)
    return result["text"]
