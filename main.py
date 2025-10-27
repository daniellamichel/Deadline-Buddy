from dotenv import load_dotenv
import os
import time
from datetime import datetime, timedelta
from plyer import notification
from twilio.rest import Client

# Load environment variables
load_dotenv()

EMAIL_ADDRESS = os.getenv("daniellajeanmichel@gmail.com")
EMAIL_APP_PASSWORD = os.getenv("EarlAandMiloCats")
TMO_NUMBER = os.getenv("6178662440")  # 10 digits only
LOCAL_TZ = ZoneInfo(os.getenv("TIMEZONE", "America/New_York"))
POLL_SECONDS = int(os.getenv("POLL_SECONDS", "900"))  # default 15 min

SMS_TO = f"{6178662440}@tmomail.net"
SENT_LOG_PATH = Path("sent_log.json")

# ---- SIMPLE ASSIGNMENT LIST ----
# Format: ("Course", "Assignment Title", "YYYY-MM-DD HH:MM")
assignments = [
    ("CS350", "Homework 3 - Trees", "2025-10-25 23:59"),
    ("CS400", "Project 1 - Wordle Game", "2025-10-30 17:00"),
]


# Function to send SMS
def send_text(course, title, due_str, hours_left):
    body = f"Reminder: {course} - {title} is due {due_str} ({hours_left}h left)!"
    message = client.messages.create(
        body=body, messaging_service_sid=messaging_service_sid, to=my_number
    )
    print("SMS sent:", message.sid)


# Function to show desktop notification
def send_desktop(course, title, due_str, hours_left):
    notification.notify(
        title="Assignment Reminder",
        message=f"{course}: {title} due {due_str} ({hours_left}h left)",
        timeout=10,
    )


# Main loop
while True:
    now = datetime.now()
    for course, title, due_str in assignments:
        due = datetime.strptime(due_str, "%Y-%m-%d %H:%M")
        hours_left = (due - now).total_seconds() // 3600

        # Trigger reminders at 72h, 24h, or same-day morning
        if hours_left in [72, 24] or (0 <= hours_left < 12 and now.hour == 9):
            print(f"Reminder: {course} - {title} is due soon!")
            send_desktop(course, title, due_str, hours_left)
            send_text(course, title, due_str, hours_left)

    # Check every hour
    time.sleep(3600)
