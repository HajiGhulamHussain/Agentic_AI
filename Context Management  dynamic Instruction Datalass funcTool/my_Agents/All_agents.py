from agents import Agent
from new_tools.math_toolss import plus,subtract,multiply,divide
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX
from context_manage import get_age
from Instruction.dynamic_instruction import dynamic_instruction
from user_Data_type.user_data import UserDataType

assistant =Agent[UserDataType](
    name="Assistant",
    instructions=dynamic_instruction,
    tools=[get_age]
)


# for check agent working
# for ag in assistant.handoffs:
    # print(f"{ag.name}: {ag.instructions}")


