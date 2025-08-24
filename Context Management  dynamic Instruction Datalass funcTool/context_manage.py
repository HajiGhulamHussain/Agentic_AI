from agents import function_tool,RunContextWrapper
from user_Data_type.user_data import UserDataType

@function_tool
def get_age(ctx: RunContextWrapper[UserDataType]): # UserDataType aur isko hum generax kaheen gy
    """age function tool"""
    print("Age tool ---> ")
    # print("ctx ---> ", ctx.context) # get full dict
    # print("ctx by name ---> ", ctx.context.name) #get only name
    return f"your age is {ctx.context.age}."
