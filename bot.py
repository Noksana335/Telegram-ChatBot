import asyncio
import logging
import os
from typing import Final

from dotenv import load_dotenv
from telegram import Update
from telegram.constants import ParseMode
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

from nlp_utils import EmotionDetector, build_response_for_emotion


# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_mention = update.effective_user.mention_html() if update.effective_user else "there"
    welcome = (
        f"Hi {user_mention}! I’m your Mental Health Self-Care Assistant.\n\n"
        "Send me a message about how you’re feeling, and I’ll respond with a supportive suggestion.\n"
        "I can recognize sadness, stress, anger, happiness, or I’ll share a general supportive note."
    )
    await update.message.reply_html(welcome)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = (
        "Send me any message about how you feel. I’ll try to detect your emotion and offer a gentle suggestion.\n"
        "Emotions: sadness, stress, anger, happiness, or unknown."
    )
    await update.message.reply_text(help_text)


async def analyze_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not update.message or not update.message.text:
        return
    text = update.message.text
    logger.info("Received message: %s", text)

    detector: EmotionDetector = context.bot_data.get("detector")
    if detector is None:
        detector = EmotionDetector()
        context.bot_data["detector"] = detector

    emotion = detector.detect_emotion(text)
    response = build_response_for_emotion(emotion)

    logger.info("Detected emotion: %s", emotion)
    await update.message.reply_text(response)


def build_application(token: str) -> Application:
    app = (
        Application.builder()
        .token(token)
        .build()
    )

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, analyze_message))
    return app


def main() -> None:
    load_dotenv()
    token: Final[str] = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
    if not token:
        logger.error("TELEGRAM_BOT_TOKEN not set. Use environment variable or .env file.")
        raise SystemExit(1)

    app = build_application(token)
    logger.info("Starting bot...")
    app.run_polling(close_loop=False)


if __name__ == "__main__":
    main()

