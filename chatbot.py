from dotenv import load_dotenv
load_dotenv()
import os
api_key = os.getenv("API_KEY")

## 

from openai import OpenAI

client = OpenAI(
   
    api_key=api_key,
)


def gpt_output(user_content):
    user_content = input("Ask me any question:  ")
    conversation = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_content}
        
    ]

    response = client.chat.completions.create(
         model="gpt-3.5-turbo",
         messages=conversation,         
         temperature=1,
         max_tokens=256,
         top_p=1,
         frequency_penalty=0,
         presence_penalty=0
   
)
 
    print("AI Response:  ", response.choices[0].message.content)
gpt_output(user_content="")

while True:
    gpt_output(user_content=None)
