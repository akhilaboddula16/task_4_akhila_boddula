import os
import subprocess


def extract_audio_from_video(video_path: str, output_audio_path: str) -> str:
    video_path = os.path.abspath(video_path)
    output_audio_path = os.path.abspath(output_audio_path)

    command = [
        "ffmpeg",
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