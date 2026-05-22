import os
import sys
import streamlit as st

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from backend.config import UPLOAD_DIR, OUTPUT_DIR
from backend.step_1_audio_extractor import extract_audio_from_video
from backend.step_2_transcriber import transcribe_audio
from backend.step_3_segment_generator import generate_viral_segments
from backend.step_4_caption_generator import generate_captions_and_headlines
from backend.step_5_broll_generator import generate_broll_ideas


st.set_page_config(
    page_title="AI Multimodal Content Engine",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 AI Multimodal Content Engine")
st.write(
    "Upload a video or audio file. The app transcribes it and generates shorts ideas, "
    "captions, viral headlines, summaries, and B-roll suggestions."
)

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

uploaded_file = st.file_uploader(
    "Upload video/audio file",
    type=["mp4", "mov", "mkv", "mp3", "wav", "m4a"]
)

whisper_model = st.selectbox(
    "Choose Whisper model",
    ["base", "small"],
    index=0
)

if uploaded_file:
    file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("File uploaded successfully.")

    if uploaded_file.name.lower().endswith((".mp4", ".mov", ".mkv")):
        st.video(file_path)
    else:
        st.audio(file_path)

    if st.button("Generate Content Assets"):
        try:
            with st.spinner("Step 1: Preparing audio..."):
                if uploaded_file.name.lower().endswith((".mp4", ".mov", ".mkv")):
                    audio_path = os.path.join(OUTPUT_DIR, "extracted_audio.wav")
                    extract_audio_from_video(file_path, audio_path)
                else:
                    audio_path = file_path

            with st.spinner("Step 2: Transcribing audio using Whisper..."):
                result = transcribe_audio(audio_path, whisper_model)
                transcript = result["text"]

            st.subheader("📝 Transcript")
            st.write(transcript)

            col1, col2 = st.columns(2)

            with col1:
                with st.spinner("Step 3: Generating viral segments..."):
                    segments = generate_viral_segments(transcript)

                st.subheader("🔥 Viral Shorts Segments")
                st.markdown(segments)

                with st.spinner("Step 4: Generating captions and headlines..."):
                    captions = generate_captions_and_headlines(transcript)

                st.subheader("📢 Captions and Headlines")
                st.markdown(captions)

            with col2:
                with st.spinner("Step 5: Generating B-roll ideas..."):
                    broll = generate_broll_ideas(transcript)

                st.subheader("🎥 AI-Suggested B-roll Ideas")
                st.markdown(broll)

            output_text_path = os.path.join(OUTPUT_DIR, "content_assets.txt")
            with open(output_text_path, "w", encoding="utf-8") as f:
                f.write("TRANSCRIPT\n")
                f.write(transcript)
                f.write("\n\nVIRAL SEGMENTS\n")
                f.write(segments)
                f.write("\n\nCAPTIONS AND HEADLINES\n")
                f.write(captions)
                f.write("\n\nB-ROLL IDEAS\n")
                f.write(broll)

            with open(output_text_path, "rb") as f:
                st.download_button(
                    "Download Generated Content Assets",
                    f,
                    file_name="content_assets.txt"
                )

        except Exception as e:
            st.error(f"Error: {e}")
