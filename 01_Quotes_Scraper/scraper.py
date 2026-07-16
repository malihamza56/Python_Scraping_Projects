"""
SCRAPER MODULE SCRAP ALL THE QUOTES FROM WEB PAGES
"""


import requests
from logger import logger

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
    