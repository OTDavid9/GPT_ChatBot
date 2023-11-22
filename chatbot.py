from dotenv import load_dotenv
load_dotenv()
import os
api_key = os.getenv("API_KEY")

## 

from openai import OpenAI

client = OpenAI(
   
    api_key=api_key,
)

user_content = input("Ask me any question:  ")
def gpt_output(user_content):

    

    conversation = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_content}
        # Add more user and assistant messages as needed
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
 
    
    print(response.choices[0].message.content)


gpt_output(user_content)
