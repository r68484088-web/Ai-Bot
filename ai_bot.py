import os
import time
import google.generativeai as genai
from pytchat import create
import sys

# API Setup
GEMINI_KEY = os.environ.get("GEMINI_KEY")
YT_API_KEY = os.environ.get("YT_API_KEY")
# TRICK: Yahan apni 11-digit ID dalo, koi extra space mat chhorna
VIDEO_ID = "RhVzkdRIQZs".strip() 

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-pro')

def get_ai_reply(text):
    try:
        response = model.generate_content(f"Reply in 1 very short Hinglish sentence: {text}")
        return response.text
    except:
        return "AI busy hai!"

def start_bot():
    print(f"Connecting to Chat ID: {VIDEO_ID}...")
    try:
        # Trick: Hum direct chat create karne se pehle 5 second wait karenge
        time.sleep(5)
        chat = create(video_id=VIDEO_ID)
        
        if not chat.is_alive():
            print("Chat is not alive. Make sure your stream is PUBLIC and LIVE.")
            return

        print("--- AI Bot is now Active! ---")
        while chat.is_alive():
            for c in chat.get().sync_items():
                if c.message.startswith("!ai"):
                    query = c.message.replace("!ai", "").strip()
                    reply = get_ai_reply(query)
                    print(f"User: {c.author.name} | AI: {reply}")
            time.sleep(1)
            
    except Exception as e:
        print(f"TRICK FAILED: {e}")
        print("Tip: Restart your stream and use the NEW video ID.")

if __name__ == "__main__":
    start_bot()
