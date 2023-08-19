import urllib

import aiohttp
import feedparser
import requests
import xmltodict
from bs4 import BeautifulSoup
from dateparser import parse as parse_date
from loguru import logger

from headlinehunt.config import settings
from headlinehunt.provider import AlphaVantage, FinnHub, GNews, GoogleNews, NewsPlease

# class Newsroom


class Headliner:
    def __init__(self):
        """
        Initialize the Headliner class

        Args:
            None
        """

        self.logger = logger
        self.enabled = settings.headliner_enabled
        if not self.enabled:
            return
        self.news_feed = settings.news_rss_url
        self.news_source = None
        self.search_source = None

    async def get_headliner_info(self):
        return

    async def get_provider(self):
        return

    async def fetch_feed(self):
        """
        Asynchronously fetches a news rss feed from the specified URL.

        :return: The formatted news feed as a string with an HTML link.
        :rtype: str or None
        """
        async with aiohttp.ClientSession() as session:
            async with session.get(settings.news_feed, timeout=10) as response:
                self.logger.debug("Fetching news from {}", settings.news_feed)
                data = (
                    xmltodict.parse(await response.text())
                    .get("rss")
                    .get("channel")["item"][0]
                )
                title = data["title"]
                link = data["link"]
                return f"📰 <a href='{link}'>{title}</a>"
