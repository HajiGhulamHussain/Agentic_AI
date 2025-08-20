# from decouple import config
import os
from dotenv import load_dotenv
from agents import AsyncOpenAI,OpenAIChatCompletionsModel,RunConfig
from agents import Agent,Runner
from new_tools.math_toolss import plus,subtract,multiply,divide
from new_tools.api_user import fetch_user_data,fetch_user_data_by_id

load_dotenv()
Gemini_client =AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

GEMINI_MODEL =OpenAIChatCompletionsModel(
    openai_client=Gemini_client,
    model="gemini-2.5-flash"
)

Gemini_config =RunConfig(
    model=GEMINI_MODEL,
    model_provider=Gemini_client,
    tracing_disabled=True
)



