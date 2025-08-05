from bio_news_etl.parser import extract_articles_from_listing

def test_article_extraction():
    with open("tests/fixtures/pnas_latest.htm", "r", encoding="utf-8") as f:
        html = f.read()
    articles = extract_articles_from_listing(html)
    assert len(articles) > 0