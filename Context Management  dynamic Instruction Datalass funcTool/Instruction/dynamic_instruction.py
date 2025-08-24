from agents import RunContextWrapper,Agent
from user_Data_type.user_data import UserDataType

def dynamic_instruction(ctx: RunContextWrapper[UserDataType],agent:Agent[UserDataType]):
    return f"user name is {ctx.context.name}, You are a helpful assistant"