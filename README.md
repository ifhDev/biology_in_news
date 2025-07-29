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
├─ scraper.py # fetch_listing_html(…)  
├─ parser.py # extract_articles_from_listing(…)  
├─ cleaner.py # clean_article_data(…)  
├─ utils.py # make_article_id(…)  
└─ dbentry.py # class ArticleDuckDB(add_article, …)  

scripts/ # CLI wrappers (empty for now)  
tests/ # unit / integration tests (empty)  
main.py # will orchestrate the pipeline  
README.md  
pyproject.toml # deps / packaging  

---

## Status

* Building phase: only dummy functions & class stubs committed.  
* Structure may shift as real logic lands.  
* No external data or credentials needed yet.

---

> Feedback, issue reports, or PRs are welcome while I learn.
