"""
_EXPORTING RAW HTML OF
HOME PAGE TO RAW DATA_
"""

from logger import logger
from config import BASE_URL,HEADERS,TIMEOUT


def export_html(html : str):
    
    """
    _EXPORT HTML TO RAW DATA_
    """
    try :
        
        logger.info("Exporting HTML to Raw Data...")
        
        with open(
            
            "data/raw/raw_html.html",
            'w',
            encoding="utf8"
            
        ) as f:
            
            f.write(html)
        
        logger.info("HTML export successfully !")
        
    except Exception as e:
        logger.error(f"Exportation Failed | {e}")
        raise
    
