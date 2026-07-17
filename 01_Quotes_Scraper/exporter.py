"""
_EXPORTING RAW HTML OF
HOME PAGE TO RAW DATA_
"""

import pandas as pd
from logger import logger



def export_html(html : str):
    
    """
    _EXPORT HTML TO RAW DATA_
    """
    try :
        
        logger.info("Exporting HTML to Raw Data...")
        
        with open(
            
            "data/raw/raw_html.html",
            'w',
            encoding="utf-8"
            
        ) as f:
            
            f.write(html)
        
        logger.info("HTML export successfully !")
        
    except Exception as e:
        logger.error(f"Exportation Failed | {e}")
        raise
    
    

#PROCESSED DATA EXPORT FUNCTIONS

def json_data(dataframes):
    
    
    try:
        
        logger.info("Quotes are converted to Json...")
        
        dataframes.to_json(
            "data/processed/quotes.json",
            orient="records",
            indent=4,
            force_ascii=False,
            )
        
        logger.info("Quotes Converted to Json Successfully !")
        
    except Exception as e:
        logger.error(f"Json conversion Failed | {e}")
        raise
    
def csv_data(dataframes):
    
    
    try:
        logger.info("Quotes are converted to CSV...")
        
        dataframes.to_csv(
            "data/processed/quotes.csv",
            index=False
        )
        
        logger.info("Quotes Converted to CSV Successfully !")
        
    except Exception as e:
        logger.error(f"CSV conversion Failed | {e}")
        raise
    
    
def excel_data(dataframes):
    
    try:
        
        logger.info("Quotes are converted to Excel...")
        
        dataframes.to_excel(
            "data/processed/quotes.xlsx",
            index=False
        )
    
        logger.info("Quotes Converted to Excel Successfully !")
        
    except Exception as e:
        logger.error(f"Excel Conversion Failed | {e}")
        raise