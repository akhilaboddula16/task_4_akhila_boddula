from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from backend.config import GROQ_API_KEY, GROQ_MODEL


def generate_broll_ideas(transcript: str) -> str:
    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model=GROQ_MODEL,
        temperature=0.5
    )

    prompt = ChatPromptTemplate.from_template("""
You are a video editor and creative director.

Based on this transcript, suggest B-roll shots.

For each B-roll idea, include:
1. Scene description
2. Visual style
3. When to use it
4. Suggested text overlay
5. Sound effect idea

Transcript:
{transcript}

Return the output in markdown.
""")

    response = llm.invoke(prompt.format_messages(transcript=transcript))
    return response.content
