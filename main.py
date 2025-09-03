from bio_news_etl import *
WEBSITES = ["tests/fixtures/pnas_latest.htm"]

def main():
    """
    Main pipeline: scrape, parse, clean, hash, and store articles in DuckDB.
    Prints count of articles found and a sample article at the end.
    """
    
    db = ArticleDuckDB()

    for website in WEBSITES:
        print(f"Processing {website}")
        articles = extract(website)

        # clean
        db.add_articles(articles)

    # check results
    db.preview(5)
    db.close()


if __name__ == "__main__":
    main()