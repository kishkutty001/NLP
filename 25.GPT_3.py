import openai

openai.api_key = "YOUR_OPENAI_API_KEY"
prompt = "Once upon a time, in a distant land,"

response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=50)
print(response["choices"][0]["text"])
