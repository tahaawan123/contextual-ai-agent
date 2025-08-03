from agents import Agent,Runner,RunContextWrapper,function_tool
from dataclasses import dataclass
import asyncio
from config import config

@dataclass
class User_Info:
    name: str
    age : int
    uid : int


@function_tool
async def fetch_user_data(wrappaer:RunContextWrapper[User_Info]):
    user = wrappaer.context

    return f" Name:  {user.name} Age: {user.age} UID: {user.uid}"


async def main():
    user_info = User_Info(name="Taha",age="24",uid=335839)


    agent =Agent[User_Info](
        name="Assistant",
        instructions="""You are a helpful assistant. When the user asks for any information 
    "related to the user's name, age, or UID, use the 'fetch_user_data' tool 
    to get the information from the provided context. Only respond using the tool's output.""",
        tools=[fetch_user_data]
    )


    result = await Runner.run(
        starting_agent=agent,
        input= "Please provide the user's name and age.",
        run_config=config,
        context=user_info

    )

    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())

