### Mental Health Self-Care Assistant (Telegram Bot)

A simple Telegram chatbot that uses spaCy NLP to detect user emotions and respond with supportive, empathetic suggestions. The bot classifies incoming messages into one of: sadness, stress, anger, happiness, or unknown, and replies with context-appropriate encouragement.

## Problem
Supporting emotional well-being is important, but many people lack quick, accessible tools for self-check-ins. This project provides a lightweight, rule-based assistant that recognizes common emotions in text and offers brief, self-care oriented suggestions. It is not a substitute for professional care, but can help users pause, reflect, and consider gentle next steps.

## Features
- Emotion detection for: sadness, stress, anger, happiness, and unknown
- Supportive responses tailored to each emotion (e.g., breathing exercises for stress, journaling for sadness, celebration for happiness)
- Fallback motivational responses when emotion is unknown
- Logging for debugging

## Tech Stack
- python-telegram-bot (v20+)
- spaCy with the `en_core_web_sm` model

## Repository Structure
```
bot.py              # Main Telegram bot
nlp_utils.py        # spaCy-based emotion detection and responses
requirements.txt    # Pinned dependencies
README.md           # Project description, setup, usage, limitations
.gitignore          # Ignore venv, caches, .env, etc.
```

## Setup
1) Create and activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

2) Install dependencies (pinned)
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

Note: The `en_core_web_sm` model is included via a pinned wheel URL in `requirements.txt`. If installation fails due to platform constraints, you can alternatively run:
```bash
python -m spacy download en_core_web_sm
```

3) Configure your Telegram Bot token
- Option A: Environment variable
```bash
export TELEGRAM_BOT_TOKEN="YOUR_TELEGRAM_BOT_TOKEN"
```

- Option B: `.env` file (loaded via `python-dotenv`)
Create a file named `.env` in the project root:
```bash
echo "TELEGRAM_BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN" > .env
```

4) Run the bot
```bash
python bot.py
```

## Usage and Verification
Open a chat with your bot in Telegram and send messages to test emotion detection:
- Sadness: "I feel so down today" → Expect empathetic message encouraging journaling or reaching out to a friend
- Stress: "I'm overwhelmed with deadlines" → Expect calming techniques like breathing exercises and short breaks
- Anger: "I'm mad about what happened" → Expect pause and de-escalation tips
- Happiness: "I had a great day!" → Expect celebration and positive reinforcement
- Unknown: Any neutral or ambiguous message → Expect generic supportive motivation

## Limitations
- Rule-based emotion detection is simplistic and may misinterpret messages
- Not a replacement for professional mental health care
- English-only support
- Context awareness is limited; nuanced or mixed emotions cannot be identified properly

## Development Notes
- Logging is enabled in `bot.py` for debugging. Increase or decrease verbosity as needed.
- The bot uses python-telegram-bot v20+ (async API); handlers are `async def`.

## Example: Setting the token in code (optional)
If you prefer to set the token directly in code (not recommended for production), you can modify `bot.py`:
```python
# In bot.py (example only; prefer environment variables or .env)
TELEGRAM_BOT_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
# Then pass TELEGRAM_BOT_TOKEN to the Application builder
```

## Disclaimer
This bot does not provide medical advice and is not a substitute for professional diagnosis or treatment. If you are in crisis or need immediate help, contact your local emergency number or a crisis hotline.

# Telegram-ChatBot
A Telegram ChatBot that uses NLP 
