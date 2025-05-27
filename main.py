import os

def main():
    api_key = os.getenv("API_KEY")
    print(f"Calling external API with key: {api_key[:4]}*** (hidden)")
    if not api_key:
        print("No API key provided!")
        return
    # Simulate calling an external API

if __name__ == "_main_":
    main()
