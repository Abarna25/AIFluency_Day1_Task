import json

from config import client,MODEL,QUESTIONS
from tools import TOOLS,TOOL_FUNCTIONS

SYSTEM_PROMPT = """
You are a student marks assistant.

Always use get_mark tool
whenever student marks are needed.
"""

def agent(question):

    messages = [
        {"role":"system","content":SYSTEM_PROMPT},
        {"role":"user","content":question}
    ]

    response = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        tools=TOOLS
    )

    message = response.choices[0].message

    if message.tool_calls:

        call = message.tool_calls[0]

        args = json.loads(call.function.arguments)

        result = TOOL_FUNCTIONS[call.function.name](**args)

        print("Tool used:",call.function.name,args)

        messages.append(message)

        messages.append({
            "role":"tool",
            "tool_call_id":call.id,
            "content":str(result)
        })

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages
        )

        return response.choices[0].message.content

    return message.content


print("=== AI AGENT ===")

for q in QUESTIONS:
    print("Q:",q)
    print("A:",agent(q))
    print("-"*50)