import os
import threading
import time
import uvicorn

def run_api():
    from main_api import app
    port = int(os.getenv("PORT", "8001"))
    uvicorn.run(app, host="0.0.0.0", port=port, log_level="info")

# Heroku provides one web dyno, so serve FastAPI and the Telegram bot
# from the same process.
# The bot talks to the API locally unless API_ENDPOINT is explicitly set.
os.environ.setdefault("API_ENDPOINT", f"http://127.0.0.1:{os.getenv('PORT', '8001')}")
api_thread = threading.Thread(target=run_api, daemon=True)
api_thread.start()
time.sleep(1)

# main_bot registers handlers and starts Telegram polling.
import main_bot  # noqa: E402,F401

# Keep the web process alive even if the polling thread is recreated.
while True:
    time.sleep(3600)
