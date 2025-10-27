# 📅 Deadline Buddy

Deadline Buddy is a lightweight Python script that helps students stay on top of assignments.  
It sends **desktop notifications** and **free SMS reminders** (via Gmail + T-Mobile's email-to-SMS gateway) at smart intervals before each deadline.

---

## ✨ Features

- Stores assignments with course, title, and due date/time.
- Sends **reminders at 72h, 24h, and 9:00 AM on the due date**.
- Notifies you via:
  - Desktop popup (using `plyer`)
  - Free SMS text (via `number@tmomail.net` and can swap to AT&T, Verizon, etc. by changing the gateway domain)
- Prevents duplicate notifications with a one-shot log.
- Fully configurable with a `.env` file.

---

## 🛠 Requirements

- Python 3.9+
- Gmail account with [App Passwords](https://myaccount.google.com/apppasswords) enabled
- T-Mobile phone number (10 digits, no dashes, no `+1`)

Install dependencies:

```bash
pip install python-dotenv plyer
```
