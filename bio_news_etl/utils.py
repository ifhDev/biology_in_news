import hashlib

def make_article_id(article):
    """
    Generate a unique hash ID for an article.
    
    Uses DOI and date (or title if DOI is missing), hashed with SHA256 and returned as hex-string.
    """

    base_string = ""
    if article.get("doi"):
        base_string += article["doi"]
    if article.get("date"):
        base_string += "|" + article["date"]
    # in case things go wrong
    if not base_string:
        base_string = article.get("title", "")
    
    article_id = hashlib.sha256(base_string.encode("utf-8"))
    
    return article_id.hexdigest()