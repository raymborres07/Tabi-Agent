import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from tools import search_hotels

# 1. Load credentials
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ Error: GEMINI_API_KEY not found in .env file")
    exit()

# 2. Initialize the new Client
client = genai.Client(api_key=api_key)

# 3. Create the Chat Session
# We configure it to know about your 'search_hotels' tool
chat = client.chats.create(
    model="gemini-flash-latest",
    config=types.GenerateContentConfig(
        tools=[search_hotels], # We pass the actual python function here
        automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=False)
    )
)

def talk_to_agent(user_input):
    print(f"\n👤 You: {user_input}")
    print("🤖 AI is thinking...")
    
    # The SDK handles the tool loop automatically!
    response = chat.send_message(user_input)
    
    # Print the final answer
    if response.text:
        print(f"🤖 AI: {response.text}")
    else:
        print("🤖 AI: (No text response, something might have gone wrong)")

if __name__ == "__main__":
    # Test 1: Complex query requiring the tool
    talk_to_agent("I want a high-end place in Hakone. Budget is around 60000 yen.")
    
    # Test 2: Follow-up to check memory
    talk_to_agent("Actually, that's too expensive. Is there anything in Osaka under 10000?")

if __name__ == "__main__":
    import time

    # Request 1
    talk_to_agent("I want a high-end place in Hakone. Budget is around 60000 yen.")
    
    # The Safety Pause (Wait 10 seconds to clear the buffer)
    print("\n⏳ Cooling down to avoid API limits...")
    time.sleep(10)
    
    # Request 2
    talk_to_agent("Actually, that's too expensive. Is there anything in Osaka under 10000?")