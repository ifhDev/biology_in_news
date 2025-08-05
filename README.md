# Biology-News ETL (WIP)

Tiny, fully-modular Python project that shows **Extract → Transform → Load** for biology-news listings.  
Right now every function is a *stub* — the repo is just the scaffolding.

---

## Why it exists

* Practice clean, testable, one-file-per-task Python.  
* ETL drill: grab article summaries from a listing page → tidy them → store in DuckDB so they’re queryable later.  
* Portfolio seed: easy to extend with extra sites, analytics, etc.

---

## Current layout

sample/  
├─ cleaner.py # `clean_article_data`  
├─ dbentry.py # class `ArticleDuckDB`  
├─ parser.py # `extract_articles_from_listing()`  
├─ scraper.py # `fetch_listing_html()`  
├─ utils.py # `make_article_id()`  
└─ websites.py # List of source URLs/files (`WEBSITES`)

scripts/ # CLI wrappers (empty for now)  
tests/ # unit / integration tests (only for parser so far, not yet workable from main folder)  
main.py # orchestrates the pipeline (`main()`)  
README.md  
pyproject.toml # deps / packaging  

---

## Current Status & Limitations

* pipeline is fully functional for local HTML test files.
* Direct requests to the live PNAS `/latest` page currently result in a 403 Forbidden error** (even with a realistic User-Agent header), despite robots.txt not explicitly forbidding scraping.  
  As a result, the included pipeline defaults to using a static copy (`tests/fixtures/pnas_latest.htm`) for demonstration and testing.
* The codebase is ready for real websites that allow scraping or for static archive/testing purposes.
* Future features (planned): CSV export, more flexible querying, and support for additional source sites.

---

> Feedback, issue reports, or PRs are welcome while I learn.
