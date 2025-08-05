from bs4 import BeautifulSoup

def extract_articles_from_listing(html):
    soup = BeautifulSoup(html, "html.parser")
    article_list = soup.find("ul", class_="list-unstyled")
    article_blocks = article_list.find_all("div", class_="card")

    articles = []
    for article in article_blocks:
        ar_type = article.find(class_="card__meta__type")
        date = article.find(class_="card__meta__date")
        title = article.find("h3", class_="article-title card__title")
        a_tag = title.find("a", href=True) if title else None
        author_block = article.find(class_="card-contribs")
        author_tags = author_block.find_all("li", class_="list-inline-item")
        authors = []
        for author_tag in author_tags:
            author = author_tag.find("a")
            if author:
                author_name = author.get("title", author.get_text(strip=True))
                authors.append(author_name)

        articles.append({
            "type": ar_type.get_text(strip=True) if ar_type else None,
            "date": date.get_text(strip=True) if date else None,
            "title": title.get_text(strip=True) if title else None,
            "doi": a_tag["href"] if a_tag else None,
            "authors": authors if authors else None,
        })
    print(f"Extracted {len(articles)} articles.")
    return articles




if __name__ == "__main__":
    with open("tests/fixtures/pnas_latest.htm", "r", encoding="utf-8") as f:
        html = f.read()
    articles = extract_articles_from_listing(html)
    print(articles[1])