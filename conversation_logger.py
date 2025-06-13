import time
import pyperclip
from datetime import datetime

# Output file path - change as needed
LOG_FILE = "./JUN25_LOG.txt"

# Store the previous clipboard content
previous_text = ""

print("📋 Clipboard logging started. Press Ctrl+C to stop.")

try:
    while True:
        current_text = pyperclip.paste().strip()
        if current_text and current_text != previous_text:
            timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
            with open(LOG_FILE, "a") as f:
                f.write(f"\n{timestamp}\n{current_text}\n")
            previous_text = current_text
        time.sleep(1)  # Check clipboard every second
except KeyboardInterrupt:
    print("\n🛑 Clipboard logging stopped.")
