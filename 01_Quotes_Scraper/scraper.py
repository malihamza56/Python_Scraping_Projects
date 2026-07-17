"""
SCRAPER MODULE SCRAP ALL THE QUOTES FROM WEB PAGES
"""

from config import MIN_DELAY,MAX_DELAY
import requests
from logger import logger
from parser import parse_html,extract_all_quotes,extract_next_page
import time
import random
from cli import (
    page_header,
    show_page_stats,
    show_waiting,
)


#FETCH HTML FROM WEB PAGE

def fetch_html(
    url : str,
    headers : dict,
    timeout : int,
)->requests.Response:
    
    """_FETCHING HTML WITH LOGGING AND
    EXCEPTION HANDLING_

    Returns:
        _RESPONSE OBJECT_: _A RESPONSE OBJECT WHICH 
    FURTHER USED FOR RETRIVATION_
    """
    
    logger.info(f"Fetching HTML from URL {url}")
    
    try:
        
        response = requests.get(
            url=url, 
            timeout=timeout,
            headers=headers
        )

        response.raise_for_status()
        
        logger.info("HTML fetched Successfull !")
        
        return response
    
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP Error | {e}")
        raise
    
    except requests.exceptions.ConnectionError as e:
        logger.error(f"Connection Error | {e}")
        raise
    
    except requests.exceptions.Timeout as e:
        logger.error(f"Timeout Error Occured | {e}")
        raise
    
    except Exception as e:
        logger.error(f"Scraper failed ! Error Occured | {e}")
        raise
    
    
def fetch_all_pages(
    url : str,
    timeout : int,
    headers : dict
)->list:
    
    current_url = url
    all_pages_quotes = []
    pages = 0
    try:
        
        logger.info("Starting Pagination....")
        page_number = 1
        
        while current_url:
            
            logger.info(f"Sending Request to {current_url}")
            page_header(page_number)
            
            response = fetch_html(
                url=current_url,
                headers=headers,
                timeout=timeout
            )
            page_number+=1
            soup = parse_html(response.text)
            
            quotes_sublist = extract_all_quotes(soup)
            
            all_pages_quotes.extend(quotes_sublist)
        
            logger.info(f"Extracted {len(quotes_sublist)} quotes from current page.")
            
            show_page_stats(
            page_quotes=len(quotes_sublist),
            total_quotes=len(all_pages_quotes),
            )
            
            next_page_url = extract_next_page(soup=soup,current_url=response.url)
            pages+=1
            if next_page_url:
                
                current_url = next_page_url
                time.sleep(random.uniform(MIN_DELAY,MAX_DELAY))
                
            
            else:
                logger.info("No next page found. Scraping completed.")
                break
         
        return all_pages_quotes,pages
    
    except Exception as e:
        logger.error(f"Pagination Failed | {e}")
        raise
    
    
    
        
        
            
            