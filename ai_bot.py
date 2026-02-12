import os
import time
import google.generativeai as genai
from pytchat import create

# Gemini Setup
genai.configure(api_key=os.environ["GEMINI_KEY"])
model = genai.GenerativeModel('gemini-pro')

def get_ai_reply(text):
    try:
        response = model.generate_content(f"Give a very short 1-line reply in Hinglish: {text}")
        return response.text
    except:
        return "AI is sleeping..."

# YouTube Live Video ID
video_id = "RhVzkdRIQZs" 
chat = create(video_id=video_id)

print("Bot is listening to chat...")
while chat.is_alive():
    for c in chat.get().sync_items():
        if c.message.startswith("!ai"):
            query = c.message.replace("!ai", "").strip()
            reply = get_ai_reply(query)
            # Ye chat mein reply print karega (Console/Logs mein dikhega)
            print(f"User: {c.author.name} | Query: {query} | AI: {reply}")
    time.sleep(2)
