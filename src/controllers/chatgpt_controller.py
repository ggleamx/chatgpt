import os
import openai

class GPT3Service:
    def __init__(self):
        openai.organization = "org-75siKsT6tKoPm4E8NR4L3qBq"
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def ask_gpt(self, question):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=question,
            max_tokens=150
        )
        return response.choices[0].text

# Create an instance of GPT3Service to be used by the route
ask_gpt = GPT3Service().ask_gpt
