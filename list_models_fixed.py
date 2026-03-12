import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("API Key not found in environment")
else:
    try:
        genai.configure(api_key=api_key)
        print("Models Available:")
        with open("models_list.txt", "w") as f:
            for m in genai.list_models():
                if 'generateContent' in m.supported_generation_methods:
                    f.write(f"{m.name}\n")
                    print(f" - {m.name}")
        print("Model list saved to models_list.txt")
    except Exception as e:
        print(f"Error listing models: {e}")
