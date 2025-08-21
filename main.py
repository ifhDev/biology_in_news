from bio_news_etl import *
WEBSITES = ["tests/fixtures/pnas_latest.htm"]


def extract(website):
    # scrape
    html = fetch_listing_html(website)
    # parse
    articles = extract_articles_from_listing(html)

    return articles

def update_db(db,articles):
    for article in articles:
            clean_article = clean_article_data(article)
            # create ID
            clean_article["article_id"] = make_article_id(clean_article)
            # insert into db
            db.add_article(clean_article)
    
def get_articles_from_db(db,number):

    results = db.query_articles()
    if results:
        for result in results[:number]:
             print(result)

     
        
def analysis():
     
    db = ArticleDuckDB()
    # check results
    articles_df = db.convert_article_to_df()


    db.con.close()     
    print(articles_df.head())

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
        update_db(db, articles)

    # check results
    get_articles_from_db(db,5)
    db.con.close()


if __name__ == "__main__":
#    main()
    analysis()