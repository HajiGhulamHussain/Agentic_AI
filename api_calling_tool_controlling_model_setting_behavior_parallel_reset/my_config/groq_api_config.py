from decouple import config
from agents import AsyncOpenAI,OpenAIChatCompletionsModel,set_tracing_disabled


key=config("GROQ_API_KEY")
base_url=config("BASE_URL_GROQ")

Groq_client =AsyncOpenAI(
    api_key=key,
    base_url=base_url
)
GROQ_MODEL =OpenAIChatCompletionsModel(
    openai_client=Groq_client,
    model="llama-3.3-70b-versatile"
)