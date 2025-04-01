import logging
import sys

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# file_handler = logging.FileHandler("example.log")
# logger.addHandler(file_handler)
stream_handler = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter("[%(asctime)s] %(levelname)s:%(name)s:%(lineno)d:%(message)s")
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)

logging.basicConfig(filename="example.log", level=logging.DEBUG, format="[%(asctime)s] %(levelname)s:%(name)s:%(lineno)d:%(message)s")


logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")