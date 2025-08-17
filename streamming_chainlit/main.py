import os
from dotenv import load_dotenv
from typing import cast
import chainlit as cl
from agents import Agent, Runner, AsyncOpenAI,OpenAIChatCompletionsModel
from agents.run import RunConfig

load_dotenv
api_key =os.getenv("OPENROUTER_API_KEY")
# print(api_key)
if not api_key:
    raise ValueError("key is not set plzz check .env file")

@cl.on_chat_start
async def start():

    external_client =AsyncOpenAI(
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1"
    )

    MODEL =OpenAIChatCompletionsModel(
        model="z-ai/glm-4.5-air:free",
        openai_client=external_client
    )

    config =RunConfig(
        model=MODEL,
        model_provider=external_client,
        tracing_disabled=True
    )

    cl.user_session.set("chat_history",[])
    cl.user_session.set("config",config)

    my_agent:Agent =Agent(
        name="Haji Ghulam Hussain ",
        instructions="you are helpful assistant agent, and solve the users all queries and problems"
    )

    cl.user_session.set("my_agent",my_agent)
    await cl.Message(content="Welcome to Haji Ghulam Hussain Chatbot how can i help you Today?").send()

    # user say message ko recieved karna
@cl.on_message
async def main(message: cl.Message):

    # history add karny k leye
    history =cl.user_session.get("chat_history") or []
    history.append({"role":"user", "content":message.content})

    msg=cl.Message(content="Haji Ghulam Hussain Testing Chatbot")
    await msg.send()

    my_agent:Agent =cast(Agent,cl.user_session.get("my_agent"))
    config:RunConfig =cast(RunConfig,cl.user_session.get("config"))

    try:
        print("\n CALLING_AGENT_WITH_CONTEXT \n", history,"\n")

        result = Runner.run_streamed(my_agent,history,run_config=config)
        async for event in result.stream_events():
            if event.type == "raw_response_event" and hasattr(event.data, 'delta'):
                token = event.data.delta
                await  msg.stream_token(token)
        history.append({"role":"assistant", "content": msg.content})
        cl.user_session.set("chat_history",history )

        print(f"user: {message.content}")
        print(f"Assistant: {msg.content}")
    
    except Exception as e:
        await msg.update(content=f"Error: {str(e)}") 
        print(f"Error: {str(e)}")

   