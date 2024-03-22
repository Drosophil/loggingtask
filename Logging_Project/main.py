# importing my logging infrastructure here as a package
from mylog import logger
import module1, module2  # just to show that logging works in other modules


# some sample logging
logger.warning("My stupid warning")
logger.error("My stupid error")
logger.info("Filter that NOLOG") # that will be filtered in some handlers, only root and console will show it