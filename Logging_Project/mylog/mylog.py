import logging

logging.basicConfig(
    level=logging.INFO,
    filename='mylog.log',
    format='%(asctime)s %(name)s -> %(levelname)s -> %(message)s'
)

my_formatter = logging.Formatter(
    "%(asctime)s %(filename)s - line %(lineno)d => %(levelname)s > %(message)s "
)

# implement filter
class MyFilter(logging.Filter):
    def filter(self, record):
        return not (record.msg.endswith("NOLOG"))

# implement custom handler
class MyCustomHandler(logging.Handler):
    def __init__(self, filename: str):
        super().__init__()
        self.file = open(filename, 'a')

    def emit(self, record: logging.LogRecord):
        self.file.write(self.format(record).swapcase())

    def __del__(self):
        self.file.close()

logger = logging.getLogger()

# default handlers: console, file

console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(my_formatter)

my_file = logging.FileHandler(filename="additional_log.log")
my_file.setLevel(logging.ERROR)
my_file.setFormatter(my_formatter)

my_special_file = MyCustomHandler("special.log")
my_special_file.setLevel(logging.ERROR)
my_special_file.setFormatter(my_formatter)

logger.addHandler(console)
logger.addHandler(my_file)
logger.addHandler(my_special_file)

my_file.addFilter(MyFilter())  # filter NOLOG suffixes
my_special_file.addFilter(MyFilter())  # filter NOLOG suffixes

