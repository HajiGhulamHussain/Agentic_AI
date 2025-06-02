class 1 project

STEPS
1. Install UV 
2. Create Folder 
3. Create Virtual Environment 
4. Install Python Env Package 
5. Create API Key 
6. Apply API Key in .env 
7. Install Open Al Agents 
8. Create Your First Agent 
9. Connection with Your LLM 
10. Execute/Run the Agent 

in short 

⚙️ Agentic AI – Setup Guide (Windows)

Install UV
Open PowerShell or CMD and run:
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

Create Project Folder
mkdir my-agent  
cd my-agent
Create Virtual Environment

uv venv
.venv\Scripts\activate
Install Python Environment Packages
For .env file support:

uv pip install python-dotenv
Create API Key
Visit platform.openai.com and generate an API key.

Apply API Key in .env File
Inside your project folder, create a .env file:

OPENAI_API_KEY= "your_api_key_here"
Install OpenAI Agents Package
If you're using OpenAI’s official openai package:


uv pip install openai
Create Your First Agent
Create a file agent.py and write your basic agent logic using the OpenAI API.

Connect with LLM (OpenAI)
In agent.py, load the .env and connect to OpenAI using your API key.

Run Your Agent
Execute the script:


What base_url is

Where it comes from

What it does

How to use it with Gemini instead of OpenAI

And the full example code at the end ✅

🔎 What is base_url?

base_url = "https://generativelanguage.googleapis.com/v1beta/openai/"
✅ 1. What is the source of this URL?
This is the official base URL provided by Google Gemini API.

Google has created an OpenAI-compatible endpoint so developers can use the same code and format as OpenAI, but with Google’s Gemini model under the hood.

🌐 2. Where does this link come from?
Website: https://ai.google.dev

Official Gemini API Docs:
👉 https://ai.google.dev/gemini-api/docs/openai

Google clearly states in the docs:

“This endpoint allows developers to use Gemini with OpenAI-style clients (like LangChain, OpenAI SDK, etc).”

🧠 3. What is the purpose of this base_url?
This URL gives you access to Google’s Gemini AI services, while keeping your code compatible with tools or libraries that were originally designed to talk to OpenAI’s API.

📘 Use case:
If you're using something like:


openai.ChatCompletion.create()
or

Runner.run_sync()
…then you can simply change the base_url to switch from OpenAI to Gemini, without changing the rest of your code.

📊 Simple Diagram:

                    🧠 Your App (Python)
                           |
                           ↓
         openai.ChatCompletion.create() or Runner.run_sync()
                           |
                           ↓
Instead of → https://api.openai.com/v1/chat/completions
Use this →   https://generativelanguage.googleapis.com/v1beta/openai/
                           |
                           ↓
               🔮 Gemini Model (by Google)
✅ Do I need to manually set this base_url?
Yes — if you're using a third-party OpenAI-style client like:

LangChain

LlamaIndex

agents.py (custom runner)

or your own wrapper

Then you must provide this base_url so the client knows to connect to Gemini, not OpenAI.

🧾 Final Answer (Short Summary)
Question	Answer
Source	Google Gemini API (OpenAI-compatible)
Website	https://ai.google.dev/gemini-api/docs/openai
Purpose	To let developers use OpenAI-style code to access Gemini models

🧪 Source Code Example (English Translator)
from dotenv import load_dotenv
import os
from agents import Agent, AsyncOpenAI, Runner, OpenAIChatCompletionsModel, RunConfig

# Load the API key from .env file
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Raise an error if the key is missing
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY is not set. Please ensure it is defined in your .env file.")

# Reference: https://ai.google.dev/gemini-api/docs/openai
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Define the Gemini model using OpenAI-compatible client
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

# Set up the configuration
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)


agent = Agent(
    name="Translator",
    instructions="You are a helpful translator. Always translate English sentences into clear and simple Urdu"
)

response = Runner.run_sync(
    agent,
    input="My name is Haji Ghulam Hussain, I am student in GIAIC.",
    run_config=config
)
print(response)

#Terminal final Output

RunResult:
- Last agent: Agent(name="Translator", ...)
- Final output (str):
    Okay, here are the translations:

    **Urdu:**

    میرا نام حاجی غلام حسین ہے، اور میں جی آئی اے آئی سی (GIAIC) میں طالب علم ہوں۔

    (Mera naam Haji Ghulam Hussain hai, aur mein GIAIC mein taalib-e-ilm hun.)

    **Russian:**

    Меня зовут Хаджи Гулам Хуссейн, я студент GIAIC.

    (Menya zovut Khadzhi Gulam Khussein, ya student GIAIC.)
- 1 new item(s)
- 1 raw response(s)
- 0 input guardrail result(s)
- 0 output guardrail result(s)
(See `RunResult` for more details)
(1st_class_agent) PS D:\coding\GIAIC\Agentic AI\practice

This AI translator works with Google Gemini using OpenAI-style code.

You provide English input, and it returns the translation.

You can translate into Urdu, Japanese, Russian, Chinese, German, or any other language.

To switch the language, just change the word "Urdu" to the name of your desired language.

🔁 BONUS TIP: Translate to Any Language
Just change the instructions line:


instructions="You are a helpful translator. Always translate English sentences into clear and simple Urdu and russian"
To:


instructions="You are a helpful translator. Always translate English sentences into clear and simple Japanese"
Or replace "Urdu" with:

"Russian"

"Chinese"

"German"

"Arabic"

"French"

etc.

✅ That's all you need to change to translate into any language.
