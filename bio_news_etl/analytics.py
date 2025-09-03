# not currently in use, stored functionality for later

def analysis():
     
    db = ArticleDuckDB()
    # check results
    articles_df = db.convert_article_to_df()


    db.con.close()     
    print(articles_df.head())