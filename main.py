from bio_news_etl import *

def main():
    db = ArticleDuckDB()
    for website in WEBSITES:
        print(f"Processing {website}")
        # scrape
        html = fetch_listing_html(website)
        # parse
        articles = extract_articles_from_listing(html)
        # clean
        for article in articles:
            clean_article = clean_article_data(article)
            # create ID
            clean_article["article_id"] = make_article_id(clean_article)
            # insert into db
            db.add_article(clean_article)
    # check results
    results = db.query_articles()
    print(f"\nDB now contains {len(results)} articles.")
    if results:
        print("First article in DB:", results[0])
    db.con.close()


if __name__ == "__main__":
    main()