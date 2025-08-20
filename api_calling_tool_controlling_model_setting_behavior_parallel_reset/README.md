🤖 Agentic AI with Gemini & Tools

This project demonstrates how to build Agentic AI workflows using:

Gemini API (via OpenAI-compatible interface)

Custom Agents with tool usage

Function-based Tools (Math + API User Fetching)

🚀 Features

🔢 Math operations (plus, subtract, multiply, divide)

🌍 Fetch users from JSONPlaceholder API

🧑‍🏫 Multiple Agents:

Math teacher

Bio science teacher

Agent-as-a-tool integration

🎛️ Tool use behaviors:

run_llm_again (default)

stop_on_first_tool

StopAtTools (stop on specific tool)

⚙️ Configurable model settings (auto, none, required, or custom tool)

📂 Project Structure
├── main.py                  # Entry point (Runner)
├── my_config/
│   ├── gemini_config.py     # Gemini API config
│   └── groq_api_config.py   # Example Groq config
├── my_Agents/
│   └── All_agents.py        # Agent definitions
├── new_tools/
│   ├── math_toolss.py       # Math tools
│   └── api_user.py          # API tools
└── .env                     # API keys (not committed)

⚡ Installation
1️⃣ Clone the repo
git clone https://github.com/your-username/your-repo.git
cd your-repo

2️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Setup environment variables

Create a .env file in the root folder:

GEMINI_API_KEY=your_google_api_key

▶️ Usage
Run main agent:
python main.py


Example:

Input: 2+5=?
Output: your answer is: 7

Run API User Tool:
from new_tools.api_user import fetch_user_data_by_id
print(fetch_user_data_by_id(3))

🛠️ Tools
Math Tools
@function_tool
def plus(n1: int, n2: int) -> str:
    """
    This is plus function
    """
    print("plus Tool Fire --->")
    return f"your answer is: {n1 + n2}"

API Tools
@function_tool
def fetch_user_data_by_id(id: int) -> dict:
    url = f"https://jsonplaceholder.typicode.com/users/{id}"
    res = requests.get(url)
    return res.json()

🧑‍💻 Agent Configurations
1️⃣ Agent as a Tool

You can pass one agent as a tool inside another:

my_Agent_as_tool = Agent(
    name="my_Agent",
    instructions="You are a helpful assistant.",
    tools=[
        my_Agent.as_tool(
            tool_name="math_Assistant",
            tool_description="you solve only math question"
        )
    ],
)

2️⃣ Tool Use Behavior

There are multiple strategies for controlling how tools are triggered:

tool_use_behavior = "run_llm_again"   # (default)
tool_use_behavior = "stop_on_first_tool"
tool_use_behavior = StopAtTools(stop_at_tool_names=["multiply"])

3️⃣ Model Settings

ModelSettings allow you to control how/when tools are called.

from agents import ModelSettings

# Automatic (default)
model_settings = ModelSettings(tool_choice="auto")

# Disable tool usage
model_settings = ModelSettings(tool_choice="none")

# Force tool usage even if not needed
model_settings = ModelSettings(tool_choice="required")

# Always use a specific tool
model_settings = ModelSettings(tool_choice="multiply")

# Parallel or sequential tool calls
model_settings = ModelSettings(parallel_tool_calls=True)
model_settings = ModelSettings(parallel_tool_calls=False)

# Reset tool choice after use
model_settings = ModelSettings(reset_tool_choice=True)

📘 Notes

as_tool allows agents to be reused as callable functions.

StopAtTools can restrict execution to certain tools.

ModelSettings gives fine-grained control over tool calling behavior.

🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

📜 License

MIT


---

👉 Ab README me saare **advance configuration points** aa gaye:  
- `Agent.as_tool`  
- `tool_use_behavior` (`run_llm_again`, `stop_on_first_tool`, `StopAtTools`)  
- `ModelSettings` (auto, none, required, fixed tool, parallel tool calls, reset tool choice)  

Kya aap chahte ho main iske sath **`requirements.txt`** bhi ready kar dun taki koi bhi seedha clone karke run kar sake?
