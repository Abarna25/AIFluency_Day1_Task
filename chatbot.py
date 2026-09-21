from config import client, MODEL, QUESTIONS

print("=== CHATBOT ===")

for q in QUESTIONS:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{
            "role":"user",
            "content":q
        }]
    )

    print("Q:", q)
    print("A:", response.choices[0].message.content)
    print("-"*50)