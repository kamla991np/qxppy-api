import json
import os

def load_session(user_agent=None):
    session_file = os.path.join(os.path.dirname(__file__), '..', 'session.json')

    if not os.path.exists(session_file):
        raise FileNotFoundError("session.json file not found. Please add your Quotex session cookie.")

    with open(session_file, 'r') as f:
        data = json.load(f)

    remember_web = data.get("remember_web")
    if not remember_web:
        raise ValueError("Missing 'remember_web' in session.json")

    session_headers = {
        "User-Agent": user_agent or "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
        "Accept": "*/*",
        "Cookie": f"remember_web={remember_web}",
        "Referer": "https://qxbroker.com/",
        "Origin": "https://qxbroker.com",
    }

    return session_headers
