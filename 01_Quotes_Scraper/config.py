"""
CONFIGURATION FOR QUOTES SCRAPER 
"""

#BASE URL
BASE_URL = "https://quotes.toscrape.com"

#TIME DELAYS
MAX_DELAY = 3
MIN_DELAY = 1


#TIMEOUT
TIMEOUT = 10


# HEADERS
HEADERS = {
    
    "User-Agent" : (
        
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)" 
        "AppleWebKit/537.36 (KHTML, like Gecko)" 
        "Chrome/149.0.0.0 Safari/537.36 OPR/133.0.0.0"
    )
}
