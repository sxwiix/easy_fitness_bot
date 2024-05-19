import logging
from telegram import Update
from telegram.ext import ContextTypes

from bot.handlers.Utils.info import print_update_data

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
# logging.getLogger("httpx").setLevel(logging.WARNING)
# logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print_update_data(update)
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Привет! Я бот.",
                                   )


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id,
                                   text="Извините, я не понимаю эту команду."
                                   )


