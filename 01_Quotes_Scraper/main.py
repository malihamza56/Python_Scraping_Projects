"""
MAIN MODULE : IT CONTROL WHOLE WORK FLOW OF PROJECT
"""

from config import BASE_URL,HEADERS,TIMEOUT
from scraper import fetch_all_pages,fetch_html
from logger import logger
from exporter import export_html,json_data,csv_data,excel_data
import pandas as pd
from cli import show_banner, show_project_info,show_summary,console
import time

def main():
    
    """_MAIN FUNCTION WHICH CONTROL
    THE WHOLE WORKFLOW_
    """
    
    try:
        logger.info("Scraper Started..")
        show_banner()
        start_time = time.perf_counter()
        show_project_info(
            website=BASE_URL,
            delay="1 - 3 sec",
            outputs="JSON | CSV | Excel"
        )
        
        #response object
        response = fetch_html(     
            url=BASE_URL,
            headers=HEADERS,
            timeout=TIMEOUT
        )
        
        export_html(response.text)   #raw html export
        console.print("[yellow]Starting pagination...[/yellow]")
       #pagination
        
        extracted_all_quotes,pages = fetch_all_pages(
            url=BASE_URL,
            timeout=TIMEOUT,
            headers=HEADERS
        )
        
        dataframes = pd.DataFrame(extracted_all_quotes)
        #EXPORTING FILES
        json_data(dataframes)
        csv_data(dataframes)
        excel_data(dataframes)
        elapsed = time.perf_counter() - start_time
        show_summary(elapsed=elapsed , pages=pages, quotes=len(extracted_all_quotes))
        
    except Exception as e:
        logger.error(f"Scraper failed | {e}")


if __name__ == "__main__":
    main()
