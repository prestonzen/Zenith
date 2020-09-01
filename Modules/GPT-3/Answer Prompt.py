#Respond to prompt
import openai

prompt = """We’re releasing an API for accessing new AI models developed by OpenAI. Unlike most AI systems which are designed for one use-case, the API today provides a general-purpose “text in, text out” interface, allowing users to try it on virtually any English language task. You can now request access in order to integrate the API into your product, develop an entirely new application, or help us explore the strengths and limits of this technology."""

response = openai.Completion.create(model="davinci", prompt=prompt, stop="\n", temperature=0.9, max_tokens=100)

print(response)
