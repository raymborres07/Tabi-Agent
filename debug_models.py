import os
from dotenv import load_dotenv
from google import genai

# 1. Load your key
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ Key missing!")
    exit()

# 2. Connect and ask for the menu
client = genai.Client(api_key=api_key)

print("🔍 Checking available models for your account...\n")

try:
    # We list all models and filter for the "Flash" ones (the fast/cheap ones)
    for model in client.models.list():
        if "flash" in model.name.lower():
            print(f"✅ Found: {model.name}")
            
except Exception as e:
    print(f"❌ Error listing models: {e}")