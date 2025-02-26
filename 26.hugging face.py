from transformers import pipeline

translator = pipeline("translation_en_to_fr")
text = "Hello, how are you?"
translation = translator(text)[0]['translation_text']

print(translation)
