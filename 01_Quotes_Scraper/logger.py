"""
PROVIDES A LOGGING INSTANCE FOR WHOLE SCRAPER
"""

import logging


"""
LOGGING CONFIGURATION
"""
logging.basicConfig(
    level=logging.INFO,
    filename="logs/scraper.log",
    format="%(asctime)s - %(filename)s - %(levelname)s - %(message)s",
    filemode='w'
)

logger = logging.getLogger(__name__)

