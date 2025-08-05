import duckdb


class ArticleDuckDB:
    def __init__(self, db_path="articles.duckdb"):
        self.con = duckdb.connect(db_path)
        self._create_table()

    def _create_table(self):
        self.con.execute("""
            CREATE TABLE IF NOT EXISTS articles (
                article_id TEXT PRIMARY KEY,
                type TEXT,
                date TEXT,
                title TEXT,
                doi TEXT,
                authors TEXT
            );
        """)

    def add_article(self, article):
        # re-strings
        authors_str = "; ".join(article["authors"]) if article["authors"] else ""
        self.con.execute("""
            INSERT OR IGNORE INTO articles
            (article_id, type, date, title, doi, authors)
            VALUES (?, ?, ?, ?, ?, ?);
        """, (
            article["article_id"],
            article["type"],
            article["date"],
            article["title"],
            article["doi"],
            authors_str
        ))
    
    def query_articles(self):
        full_query = self.con.execute("SELECT * FROM articles").fetchall()

        return full_query
    
    def close(self):
        self.con.close()