
from agents import Runner
from my_config.gemini_config import Gemini_config
from my_Agents.All_agents import my_Agent,my_Agent_as_tool

# Note: All_agents
# 1 agent as_tool
# 2 tool_use_behavior ="run_llm_again" = "stop_on_first_tool"  | class StopAtTools
# 3 model_setting = class hai ya b import hogi

result=Runner.run_sync(
    my_Agent, 
    input="2+5=?",
    run_config=Gemini_config,
    max_turns=4
    )
print(result.final_output)
