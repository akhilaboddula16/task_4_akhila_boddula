from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from backend.config import GROQ_API_KEY, GROQ_MODEL


def generate_captions_and_headlines(transcript: str) -> str:
    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model=GROQ_MODEL,
        temperature=0.6
    )

    prompt = ChatPromptTemplate.from_template("""
You are a social media content expert.

Using the transcript below, generate:

1. 5 viral short video titles
2. 5 Instagram Reel captions
3. 5 YouTube Shorts captions
4. 5 LinkedIn post captions
5. 5 hashtags
6. One short summary

Transcript:
{transcript}

Return the output in clean markdown.
""")

    response = llm.invoke(prompt.format_messages(transcript=transcript))
    return response.content
