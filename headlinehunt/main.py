import urllib

import feedparser
import requests
from bs4 import BeautifulSoup
from dateparser import parse as parse_date
from loguru import logger
import aiohttp
import xmltodict
from headlinehunt.config import settings

#class Newsroom



class Headliner():


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
        self.news_feed = None
        self.news_source = None
        self.search_source = None
        

    async def get_headliner_info(self):
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

# async def fetch_top_news(self):
#     try:
#         async with aiohttp.ClientSession() as session:
#             async with session.get(self.news_url, timeout=10) as response:
#                 data = await response.json()
#                 articles = data.get('articles', [])
#                 key_news = [
#                     {'title': article['title'], 'url': article['url']}
#                     for article in articles
#                 ]
#                 last_item = key_news[-1]
#                 return f"📰 <a href='{last_item['url']}'>{last_item['title']}</a>"

#     except aiohttp.ClientError as error:
#         self.logger.warning("news %s", error)
#         return None
