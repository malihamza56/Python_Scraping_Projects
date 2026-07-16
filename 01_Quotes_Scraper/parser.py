"""
PARSER WHICH PARSE THE HTML AND EXCTRACT THE REQUIRED DATA
"""

from bs4 import BeautifulSoup
from logger import logger


def parse_html(html : str):
    
    
    """_THIS FUNCTION PARSE HTML INTO A SOUP OBJECT_

    Returns:
        _SOUP OBJECT_: _SOUP OBJECT THROUGH WHICH DATA WILL BE EXTRACTED_
    """
    
    
    try:
        
        logger.info("Parsing HTML ...")
        
        soup = BeautifulSoup(html , "html.parser")
        
        logger.info("HTML Parsed Successfully !")
        
        return soup
    
    except Exception as e:
        logger.error(f"Parsing Failed | {e}")
        raise
        

       
def extract_quote(quote):
    
    """_EXTRACT QUOTE_

    Returns:
        _QUOTE_: _RETURN QUOTE TEXT _
    """
    
    try: 
        
        logger.info("Exctracting Quote...")
        
        quote_text = quote.select_one(".text")
        
        logger.info("Quote Extraction Successfully !")
        
        return quote_text.text.strip().capitalize()
    
    except Exception as e:
        logger.error(f"Exctraction Failed | {e}")
        raise
        
def extract_author(quote):
    
    """_EXTRACT AUTHOR NAME OF THAT QUOTE_

    Returns:
        _AUTHOR NAME_: _AUHTOR NAME OF THAT PARTICULAR QUOTE_
    """
    
    try:
        
        logger.info("Extracting Author Name...")
        
        author_name = quote.select_one(".author")

        logger.info("Auhtor Extraction Successfully !")
        
        return author_name.text.strip().capitalize()

    except Exception as e:
        
        logger.error(f"Extraction Failed | {e}")
        raise
        
def extract_tags(quote):
    
    
    """_EXTRACT ALL TAGS OF THAT QUOTE_

    Returns:
        _LIST_: _A LIST OF ALL THE ALL THE TAGS OF THAT QUOTE_
    """
    
    tags = [
        
    ]
    
    try:
        
        logger.info("Exctracting Tags...")
        
        tag_container = quote.select(".tag")
        
        for tag in tag_container:
            tags.append(tag.text)
            
        
        logger.info("Tags Extracted Successfully !")
        
        return tags

    except Exception as e:
        logger.error(f"Extracion Failed | {e}")
        raise
    

def extract_all_quotes(quotes):
    
    
    """_EXTRACT ALL THE QUOTES_

    Returns:
        _LIST_: _A LIST OF DICTIONARIES WHICH CONTAIN QUOTES_
    """
    quotes_list = [
        
    ]
    
    try:
        
        logger.info("Extractnig All Quotes...")
        
        for quote in quotes:
            
            quotes_list.append(
                
                {
                "quote" : extract_quote(quote=quote),
                "author" : extract_author(quote=quote),
                'tags' : extract_tags(quote=quote)
                }
            )

        logger.info("All Quotes Extracted Successfully !")
        
        return quotes_list
    
    except Exception as e:
        logger.error(f"Exctraction Failed | {e}")
        raise
    
        