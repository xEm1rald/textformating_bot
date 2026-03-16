import asyncio
import json
import urllib.parse
from datetime import timedelta, datetime

from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, Document
from telegram.ext import ContextTypes, ConversationHandler, CommandHandler, MessageHandler
from telegram.ext import filters

from bs4 import BeautifulSoup

from bs4 import BeautifulSoup
from bs4 import BeautifulSoup, NavigableString

def fix_msg(html: str) -> str:
    soup = BeautifulSoup(html, "html5lib")

    # объединять только соседние blockquote
    for bq in soup.find_all("blockquote"):
        next = bq.find_next_sibling()

        while next and next.name == "blockquote":
            #bq.append(NavigableString("\n"))
            for c in list(next.contents):
                bq.append(c)
            temp = next
            next = next.find_next_sibling()
            temp.decompose()

    # удалить пустые теги
    for tag in soup.find("body").find_all():
        if not tag.get_text(strip=True):
            tag.replace_with(NavigableString(tag.text))

    return (str(soup)
            .replace("<html><head></head><body>", "")
            .replace("</body></html>", ""))

async def parse_msg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.effective_message.text_html
    text = fix_msg(msg)

    await update.message.reply_document(
        document=text.encode(),
        filename=f"format_text_{int(datetime.now().timestamp())}.txt",
        caption=text,
        parse_mode="HTML"
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
        Bot working...
        """,
        parse_mode="HTML"
    )


start_command_handler = CommandHandler("start", start)
raw_text_handler = MessageHandler(filters.TEXT, parse_msg)