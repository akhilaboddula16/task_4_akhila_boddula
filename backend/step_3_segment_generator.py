from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from backend.config import GROQ_API_KEY, GROQ_MODEL


def generate_viral_segments(transcript: str) -> str:
    llm = ChatGroq(
        groq_api_key=GROQ_API_KEY,
        model=GROQ_MODEL,
        temperature=0.4
    )

    prompt = ChatPromptTemplate.from_template("""
You are a short-form video strategist.

From the transcript below, identify 5 short-form viral video segments.

For each segment, provide:
1. Segment title
2. Start idea / hook
3. Summary
4. Why it can go viral
5. Suggested duration
6. Target platform

Transcript:
{transcript}

Return the output in clean markdown.
""")

    response = llm.invoke(prompt.format_messages(transcript=transcript))
    return response.content
