# importing my logging infrastructure here as a package
from mylog import logging


# some sample logging
logging.warning("My stupid warning")
logging.error("My stupid error")
logging.info("Filter that NOLOG") # that will be filtered in some handlers, only root and console will show it