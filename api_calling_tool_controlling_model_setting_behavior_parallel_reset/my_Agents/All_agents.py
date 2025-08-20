from agents import Agent,ModelSettings
# from my_config.gemini_config import GEMINI_MODEL
from my_config.groq_api_config import GROQ_MODEL
from dataclasses import dataclass
from pydantic import BaseModel
from new_tools.math_toolss import plus, subtract, multiply, divide
from new_tools.api_user import fetch_user_data,fetch_user_data_by_id
from agents.agent import StopAtTools

my_Agent =Agent(
    name="my_Agent",
    instructions="You are a helpful math teacher.",
    tools=[plus,subtract,multiply,divide,fetch_user_data,fetch_user_data_by_id],
    # tool_use_behavior="run_llm_again" # bydefault yahi value set rehti hai 
    tool_use_behavior=StopAtTools(stop_at_tool_names=["plus", "multiply"]),

    # model_setting main class import hogi us k 3 para meter hain "auto","non","required"
    # auto llm ko jab zrort dekhy tu tool call hojahy ya default set hota hai 
    # none ismain tool call nai hoga bhaly zrort bhi ho 
    # required is main zrort na bhi ho tb bhi tool call hoga 
    # multiply ab ya sirf multiply kry ga bss

    model_settings=ModelSettings(tool_choice="subtract",parallel_tool_calls=False),
                                reset_tool_choice=True
 
)
bio_Science_Agent =Agent(
    name="science Assistant",
    instructions="You are a helpful bio science teacher.",
)

# Agent as tool 
my_Agent_as_tool =Agent(
    name="my_Agent",
    instructions="You are a helpful assistant.",
    tools=[
        my_Agent.as_tool
        (
        tool_name="math_Assistant",
        tool_description="you solve only math question"),

     bio_Science_Agent.as_tool(
         tool_name="science_assistant",
         tool_description="you are a helpful biology science teacher"
         # is main normal tool bhi pass kar skty hain normal function tool jo decorator say banty hain
     )],
)





# groq_agent1 =Agent(
#     name="Physics_Teacher",
#     instructions="You are a helpfull physics teacher",
#     model=GROQ_MODEL,
#     tools=[plus, subtract, multiply, Divide, fetch_user_data, fetch_user_data]
# )
