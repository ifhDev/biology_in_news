from bio_news_etl import *

def main():
    for website in WEBSITES:
        print(f"Processing {website}")
        # scrape
        html = fetch_listing_html(website)
        # parse
        articles = extract_articles_from_listing(html) # 2025/08/05 stubs start here
        # clean (currently mostly placeholder)
        for article in articles:
            clean_article = clean_article_data(article)
            # create ID
            clean_article_data['article_id'] = make_article_id(clean_article)
        # # drop into duckdb
        #     db = ArticleDuckDB()
        #     db.add_article(clean_article)
    print('Pipeline ran (most functions are still stubs).')


if __name__ == "__main__":
    main()
