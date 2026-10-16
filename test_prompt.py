import tomllib
from google import genai
from google.genai import types

MODEL = "gemini-3.5-flash-lite"

with open(".streamlit/secrets.toml", "rb") as f:
    key = tomllib.load(f)["GEMINI_API_KEY"]

client = genai.Client(api_key=key)
system = open("system_prompt.txt", encoding="utf-8").read()

message = "Congratulations! You are selected for Data Entry at Rs 45,000/month. Work from home, no interview. Pay Rs 2,000 registration fee to confirm. WhatsApp 98XXXXXXXX."

reply = client.models.generate_content(
    model=MODEL,
    contents=message,
    config=types.GenerateContentConfig(
        system_instruction=system,
        temperature=0.2,
        response_mime_type="application/json",
    ),
)
print(reply.text)