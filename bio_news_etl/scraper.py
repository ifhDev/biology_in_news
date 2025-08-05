import requests
from urllib.parse import urlparse
import time


def fetch_listing_html(site_url):
    """
    Fetch and return HTML from a URL or local file.
    
    - downloads the page if site_url starts with 'http'/'https' or 'www'.
    - otherwise, attempts to read from a local HTML file.
    Returns the page content as a string.
    """

    headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
        ),
    }
    # normalise www URLs (leftover from copy-paste)
    if site_url.startswith("www"):
        site_url = "http://" + site_url

    parsed = urlparse(site_url)

    # treat as web URL
    if parsed.scheme in ("http", "https"):
        time.sleep(1) # avoids potential server flooding
        response = requests.get(site_url, headers=headers)
        response.raise_for_status() # should create error message
        return response.text
    
    # treat as local file
    else:
        with open(site_url, "r", encoding="utf-8") as f:
            return f.read()