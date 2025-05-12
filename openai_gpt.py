from openai import OpenAI
import os

client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY")
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "What is the historic record high temperature for owatonna Minnesota on May 12th"}
  ]
)

print(completion.choices[0].message.content);