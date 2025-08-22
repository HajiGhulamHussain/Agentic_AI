from agents import Agent
from new_tools.math_toolss import plus,subtract,multiply,divide
from agents.extensions.handoff_prompt import RECOMMENDED_PROMPT_PREFIX

Math_Agent =Agent(
    name="Math Teacher",
    instructions=f"""{RECOMMENDED_PROMPT_PREFIX} You are a helpful math teacher.",
""",
    tools=[plus],
    handoff_description="This is a math teacher",
)
English_Agent =Agent(
    name="English Teacher",
    instructions=f"""{RECOMMENDED_PROMPT_PREFIX} You are a helpful English teacher.",
""",
    tools=[plus],
    handoff_description="This is a english teacher"
)

assistant =Agent(
    name="Assistant",
    instructions="You are a helpful assistant.",
    handoffs=[Math_Agent,English_Agent]
)

# for check agent working
# for ag in assistant.handoffs:
    # print(f"{ag.name}: {ag.instructions}")


