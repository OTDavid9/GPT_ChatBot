import os 
import openai

openai.api_key = os.getenv("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")
openai.Model.list()