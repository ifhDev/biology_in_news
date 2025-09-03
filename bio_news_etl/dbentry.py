import duckdb
from .cleaner import clean_article_data
from .utils import make_article_id


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

    def add_articles(self, articles):
        """
        Insert one or many articles.
        Accepts a single dict or a list of dicts.
        Cleans + assigns IDs before insert.
        """
        if isinstance(articles, dict):
            articles = [articles]

        for article in articles:
            clean = clean_article_data(article)
            clean["article_id"] = make_article_id(clean)
            authors_str = "; ".join(clean["authors"]) if clean["authors"] else ""
            self.con.execute(
                """
                INSERT OR IGNORE INTO articles
                (article_id, type, date, title, doi, authors)
                VALUES (?, ?, ?, ?, ?, ?);
                """,
                (
                    clean["article_id"],
                    clean["type"],
                    clean["date"],
                    clean["title"],
                    clean["doi"],
                    authors_str,
                )
            )

    def query_articles(self, limit=None, order_by=None):
        """Return rows as tuples; optional LIMIT and ORDER BY."""
        sql = "SELECT * FROM articles"
        if order_by:
            sql += f" ORDER BY {order_by}"
        if limit is not None:
            return self.con.execute(sql + " LIMIT ?", [limit]).fetchall()
        return self.con.execute(sql).fetchall()

    def query_articles_df(self, limit=None, order_by=None):
        """Return rows as a pandas DataFrame; optional LIMIT and ORDER BY."""
        sql = "SELECT * FROM articles"
        if order_by:
            sql += f" ORDER BY {order_by}"
        if limit is not None:
            return self.con.execute(sql + " LIMIT ?", [limit]).fetch_df()
        return self.con.execute(sql).fetch_df()

    def preview(self, n=5):
        """Print and return the first n rows as a DataFrame."""
        df = self.query_articles_df(limit=n)
        print(df)
        return df

    def close(self):
        """Close the DuckDB connection."""
        self.con.close()