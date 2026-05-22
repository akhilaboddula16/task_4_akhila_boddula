# 🎬 AI Multimodal Content Engine

An AI-powered Multimodal Content Generation system that automatically transforms videos or audio content into short-form content assets including transcripts, viral segments, social media captions, headlines, summaries, and AI-generated B-roll ideas.

This project uses Speech-to-Text and Large Language Models to automate content repurposing for creators, marketers, and social media teams.

---

# 🚀 Project Overview

Content creators often spend significant time manually creating:

- Video transcripts
- Viral short clips
- Instagram captions
- YouTube titles
- LinkedIn summaries
- B-roll ideas

This project automates the complete workflow.

Input:

```text
Video (.mp4/.mov/.mkv)
or
Audio (.mp3/.wav/.m4a)
```

Output:

```text
Transcript
↓
Viral Segments
↓
Captions
↓
Headlines
↓
Summary
↓
B-roll Suggestions
```

---

# ✨ Features

### Content Processing

✅ Upload video files

✅ Upload audio files

✅ Automatic audio extraction

✅ Speech-to-text conversion

---

### AI Content Generation

✅ Viral short-form segment generation

✅ Instagram Reel captions

✅ YouTube Shorts captions

✅ LinkedIn post captions

✅ Viral titles/headlines

✅ Summary generation

✅ Hashtag generation

---

### Creative AI Features

✅ AI-generated B-roll suggestions

✅ Scene descriptions

✅ Visual style suggestions

✅ Text overlays

✅ Sound effect recommendations

---

### User Features

✅ Streamlit UI

✅ Download generated content assets

✅ Multiple content outputs

---

# 🛠 Tech Stack

| Component | Technology |
|------------|------------|
| Frontend | Streamlit |
| Backend | Python |
| LLM | Groq |
| Speech-to-Text | OpenAI Whisper |
| Prompt Framework | LangChain |
| Audio Extraction | FFmpeg |
| Video Processing | MoviePy |
| Environment Variables | Python Dotenv |

---

# 📂 Project Structure

```text
multimodal_content_engine/

│
├── backend/
│   │
│   ├── __init__.py
│   │
│   ├── config.py
│   │
│   ├── step_1_audio_extractor.py
│   │
│   ├── step_2_transcriber.py
│   │
│   ├── step_3_segment_generator.py
│   │
│   ├── step_4_caption_generator.py
│   │
│   └── step_5_broll_generator.py
│
│
├── frontend/
│   │
│   └── app.py
│
│
├── uploads/
│
├── outputs/
│
├── .env
│
├── requirements.txt
│
└── README.md
```

---

# ⚙️ Installation

## Step 1: Clone Repository

```bash
git clone <your_repository_url>

cd multimodal_content_engine
```

---

## Step 2: Create Virtual Environment

For Python 3.11:

```bash
py -3.11 -m venv venv
```

Activate:

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

---

## Step 3: Install Dependencies

Update pip:

```bash
python -m pip install --upgrade pip
```

Install requirements:

```bash
pip install -r requirements.txt --prefer-binary
```

---

# Install FFmpeg

Required for:

- Audio extraction
- Video processing
- Whisper transcription

Windows:

```bash
winget install Gyan.FFmpeg
```

Verify:

```bash
ffmpeg -version
```

---

# 🔑 Environment Variables

Create:

```text
.env
```

Add:

```env
GROQ_API_KEY=your_groq_api_key

GROQ_MODEL=llama-3.1-8b-instant
```

Get API key:

https://console.groq.com/

---

# ▶️ Run Project

```bash
streamlit run frontend/app.py
```

Application:

```text
http://localhost:8501
```

---

# 🔄 Workflow Architecture

```text
User Uploads Video/Audio
            ↓
Audio Extraction (FFmpeg)
            ↓
Speech-to-Text (Whisper)
            ↓
Transcript Generation
            ↓
Groq LLM Processing
            ↓
Generate:
     ↓
Viral Segments
Captions
Headlines
Hashtags
Summaries
B-roll Ideas
```

---

# 📘 Module Explanation

## step_1_audio_extractor.py

Purpose:

- Extract audio from uploaded video

Functions:

```python
extract_audio_from_video()
```

Uses:

```text
FFmpeg
MoviePy
```

---

## step_2_transcriber.py

Purpose:

Convert speech into text.

Functions:

```python
transcribe_audio()
```

Uses:

```text
Whisper
```

Output:

```text
Transcript
```

---

## step_3_segment_generator.py

Purpose:

Generate viral short-form segments.

Output:

```text
Hook
Summary
Duration
Platform
```

---

## step_4_caption_generator.py

Purpose:

Generate:

- Captions
- Titles
- Headlines
- Hashtags

---

## step_5_broll_generator.py

Purpose:

Generate AI creative suggestions.

Output:

- Scene description
- Visual style
- Text overlays
- Sound effects

---

# 🧪 Example Inputs

### Video Examples

- TED Talk
- Podcast clip
- AI tutorial
- YouTube Short
- Tech explanation video

Supported formats:

```text
MP4
MOV
MKV
MP3
WAV
M4A
```

---

# 🧠 Example Output

## Transcript

```text
Today we will discuss Artificial Intelligence...
```

---

## Viral Segment

```text
Title:
AI Will Replace Jobs?

Hook:
Most people completely misunderstand AI.
```

---

## Caption

```text
AI is changing the future faster than you think 🚀
```

---

## B-roll

```text
Scene:
Person working with futuristic AI interface

Text Overlay:
Future of AI

Sound Effect:
Whoosh transition
```

---

# 🐞 Common Errors

## Error:

```text
ModuleNotFoundError:
No module named moviepy.editor
```

Solution:

Replace:

```python
from moviepy.editor import VideoFileClip
```

with:

```python
from moviepy import VideoFileClip
```

---

## Error:

```text
WinError 2:
The system cannot find file specified
```

Solution:

Install FFmpeg:

```bash
winget install Gyan.FFmpeg
```

Restart VS Code.

---

## Error:

```text
File size too large
```

Solution:

Trim video using:

- Clipchamp
- FFmpeg
- Windows Photos App

Recommended:

```text
30 sec–5 min
```

---

# 🔮 Future Improvements

- Multi-language support
- Speaker diarization
- Real-time transcription
- AI video generation
- Auto subtitles
- Multi-video processing
- YouTube API integration
- Cloud deployment
- User authentication

---

# 🌐 Live Demo

Add your deployed Streamlit link:

```text
https://your-streamlit-app.streamlit.app
```

---

# 👩‍💻 Author

Akhila Boddula

AI Engineer | Generative AI | Agentic AI | Multimodal AI

GitHub:

https://github.com/akhilaboddula16

LinkedIn:

https://www.linkedin.com/in/akhila-boddula
