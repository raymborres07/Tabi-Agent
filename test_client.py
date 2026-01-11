# We import the tool directly from your server file
from server import search_hotels

def run_test():
    print("🤖 AI: I am looking for a hotel in Kyoto under 20,000 yen...")
    
    # We call the function directly, just like a normal Python script
    result = search_hotels(location="Kyoto", max_price=20000)
    
    print("\n📦 Database Reply:")
    print(result)

if __name__ == "__main__":
    run_test()