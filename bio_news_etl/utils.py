import hashlib

def make_article_id(article):
    # creates unique id from date+url with SHA256
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