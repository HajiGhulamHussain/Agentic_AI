# Import necessary modules
from dotenv import load_dotenv  # For loading environment variables from .env file
import os  # For interacting with the operating system (to access environment variables)

# Import necessary classes from the agents package
from agents import Agent, AsyncOpenAI, Runner, OpenAIChatCompletionsModel, RunConfig

# Load environment variables from the .env file
load_dotenv()

# Get the Gemini API key from environment variables
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Check if the API key is present; if not, raise an error
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

# Reference: https://ai.google.dev/gemini-api/docs/openai
# Initialize the external OpenAI-compatible client for Gemini
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",  # Gemini's OpenAI-compatible endpoint
)

# Define the model using Gemini (OpenAI-compatible model setup)
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",  # Model name to use
    openai_client=external_client  # Use the Gemini client as the backend
)

# Create a run configuration object to define model and other settings
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True  # Disable tracing/logging (optional)
)

# Define an AI agent with a specific role and instruction
agent = Agent(
    name="Translator",  # Name of the agent
    instructions="You are a helpful translator. Always translate English sentences into clear and simple urdu and russian"
)

# Run the agent synchronously using the provided configuration and input
response = Runner.run_sync(
    agent,
    input="My name is Haji Ghulam Hussain, I am student in GIAIC.",  # Input sentence to translate
    run_config=config
)

# Print the agent's response
print(response)
