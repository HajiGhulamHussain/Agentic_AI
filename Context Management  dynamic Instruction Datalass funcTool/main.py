from agents import Runner
from my_config.gemini_config import Gemini_config
from my_Agents.All_agents import assistant
from user_Data_type.user_data import UserDataType


user_1 = UserDataType(name="Haji",age=20,role="student")

result=Runner.run_sync(
    assistant, 
    input="what is age of user? ",
    # context=["Haji Ghulam Hussain"], #str
    # context=["Noman","chaman Lal"], #list
    context=user_1, #obj
    run_config=Gemini_config,

    )
print(result.final_output)
