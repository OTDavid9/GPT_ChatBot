# import os 
# import openai
# openai.api_key  = 
# answer = openai.completion.create(
#     model = "text-davinci-003",
#     prompt = "Say this is a test",
#     max_tokens = 7,
#     temperature = 0
# )

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the API key
api_key = os.getenv("API_KEY")

# Now you can use the api_key variable in your code
print(api_key)