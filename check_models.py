import google.generativeai as genai
YOUR_API_KEY = 'your_api_key_here'

genai.configure(api_key=YOUR_API_KEY)

print("Available models for your API key:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(f"- {m.name}")