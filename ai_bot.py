import os
import time
import google.generativeai as genai
from pytchat import create
import sys

# API Setup
GEMINI_KEY = os.environ.get("GEMINI_KEY")
YT_API_KEY = os.environ.get("YT_API_KEY")
# DHAYAN DEIN: Yahan bina kisi space ke ID dalein
VIDEO_ID = "RhVzkdRIQZs" 

genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-pro')

def get_ai_reply(text):
    try:
        response = model.generate_content(f"Reply in 1 very short Hinglish sentence: {text}")
        return response.text
    except:
        return "AI thoda busy hai!"

try:
    chat = create(video_id=VIDEO_ID)
    print(f"Connected to Video ID: {VIDEO_ID}")
except Exception as e:
    print(f"Error connecting to chat: {e}")
    sys.exit(1)

while chat.is_alive():
    for c in chat.get().sync_items():
        if c.message.startswith("!ai"):
            query = c.message.replace("!ai", "").strip()
            reply = get_ai_reply(query)
            print(f"User: {c.author.name} | AI: {reply}")
    time.sleep(1)
