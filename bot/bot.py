from telegram.ext import Application, CommandHandler, CallbackQueryHandler, PreCheckoutQueryHandler, ContextTypes, ConversationHandler, MessageHandler, filters

from config import BOT_TOKEN
from . import handlers


def run():
    app = (
        Application.builder()
        .token(BOT_TOKEN)
        .build()
    )

    app.add_handlers([
        # CommandHandlers
        handlers.start_command_handler,
        handlers.raw_text_handler
    ])

    app.run_polling()


