import os

FFMPEG_BIN = r"C:\Users\karth\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.1-full_build\bin"
os.environ["PATH"] += os.pathsep + FFMPEG_BIN

import whisper


def transcribe_audio(audio_path: str, model_name: str = "base") -> dict:
    model = whisper.load_model(model_name)
    result = model.transcribe(audio_path)

    return {
        "text": result.get("text", ""),
        "segments": result.get("segments", [])
    }