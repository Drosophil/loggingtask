import logging
import os

# import telebot

# TG_BOT_TOKEN = os.getenv("TG_BOT_TOKEN")
# CHAT_ID = os.getenv("CHAT_ID")

logging.basicConfig(
    level=logging.INFO,
    filename='mylog.log',
    format='%(asctime)s %(name)s -> %(levelname)s -> %(message)s'
)

my_formatter = logging.Formatter(
    "%(asctime)s %(filename)s - line %(lineno)d => %(levelname)s > %(message)s "
)

logger = logging.getLogger()
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
console.setFormatter(my_formatter)

logger.addHandler(console)

"""
class MyGreatHandler(logging.Handler):
    def __init__(self, my_filename: str):
        super().__init__()
        self.my_filename = my_filename

    def emit(self, record: logging.LogRecord):
        bot = telebot.TeleBot(self.api_key)

        bot.send_message(
            self.chat_id,
            self.format(record)
        )


class TestFilter(logging.Filter):

    def filter(self, record):
        # Returns False if battle finished with a draw
        return not (record.msg.lower().startswith('test'))


root_logger = logging.getLogger()

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
console.setFormatter(main_formatter)

file = logging.FileHandler(filename="important_logs.txt")
file.setLevel(logging.ERROR)
file.setFormatter(main_formatter)

telegram = TelegramBotHandler(TG_BOT_TOKEN, CHAT_ID)
telegram.setLevel(logging.ERROR)
telegram.setFormatter(main_formatter)

root_logger.addHandler(console)
root_logger.addHandler(file)
root_logger.addHandler(telegram)

telegram.addFilter(TestFilter())
"""