from agents import Runner
from my_config.gemini_config import Gemini_config
from my_Agents.All_agents import Math_Agent,English_Agent,assistant


result=Runner.run_sync(
    assistant, 
    # input="2+2=?",
    # input="what is fundamental of english answer in short 1 line",
    input="Hello",
    run_config=Gemini_config,

    )
print(f"Agent Name: {result.last_agent.name}")# check karny k leye k kis agent nay jawab dia hai 
print(result.final_output)
