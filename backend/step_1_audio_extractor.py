import os
import subprocess

FFMPEG_PATH = r"C:\Users\karth\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1.1-full_build\bin\ffmpeg.exe"


def extract_audio_from_video(video_path: str, output_audio_path: str) -> str:
    video_path = os.path.abspath(video_path)
    output_audio_path = os.path.abspath(output_audio_path)

    command = [
        FFMPEG_PATH,
        "-y",
        "-i", video_path,
        "-vn",
        "-acodec", "pcm_s16le",
        "-ar", "16000",
        "-ac", "1",
        output_audio_path
    ]

    subprocess.run(command, check=True)

    return output_audio_path