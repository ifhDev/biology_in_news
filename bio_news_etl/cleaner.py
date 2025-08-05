def clean_article_data(article):
    # standardises/validates fields
    required_fields = {
        "type": None,
        "date": None,
        "title": "",
        "doi": None,
        "authors": [],
    }
    for key, default in required_fields.items():
        if key not in article or article[key] is None or article[key] == "":
            article[key] = default
    authors = article.get("authors")
    if isinstance(authors, str):
        # in case author splitting didn't work on entry
        if ";" in authors:
            # for publications that use the "Surname, Name" splitting
            author_list = [a.strip() for a in authors.split(";") if a.strip()]
        else:
            # for everything else
            author_list = [a.strip() for a in authors.split(",") if a.strip()]
        article["authors"] = author_list
    elif authors is None:
        article["authors"] = []
    return article