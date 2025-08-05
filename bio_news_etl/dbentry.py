import duckdb


class ArticleDuckDB:
    """Database handler for storing and querying articles in DuckDB."""

    def __init__(self, db_path="articles.duckdb"):
        self.con = duckdb.connect(db_path)
        self._create_table()

    def _create_table(self):
        """Initialize connection and create articles table if needed."""
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
        """Insert a cleaned article into the DB (ignores duplicates)."""
        
        authors_str = "; ".join(article["authors"]) if article["authors"] else "" # re-strings
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
        """Return all articles as a list of tuples."""

        full_query = self.con.execute("SELECT * FROM articles").fetchall()

        return full_query
    
    def close(self):
        """Close the DuckDB connection."""
        
        self.con.close()