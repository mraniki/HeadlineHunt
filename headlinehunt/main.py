import urllib

import feedparser
import requests
from bs4 import BeautifulSoup
from dateparser import parse as parse_date
from loguru import logger

from headlinehunt.config import settings

#class Newsroom



class Headliner


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
        self.news_source = 
        self.search_source = 
        

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



    def top_news(self):
        """Return a list of all articles from the main page of Google News
        given a country and a language"""
        d = self.__parse_feed(
            self.BASE_URL + self.__ceid()
        )
        d["entries"] = self.__add_sub_articles(d["entries"])
        return d

    def topic_headlines(self, topic: str):
        """Return a list of all articles from the topic page of Google News
        given a country and a language"""
        # topic = topic.upper()
        if topic.upper() in [
            "WORLD",
            "NATION",
            "BUSINESS",
            "TECHNOLOGY",
            "ENTERTAINMENT",
            "SCIENCE",
            "SPORTS",
            "HEALTH",
        ]:
            d = self.__parse_feed(
                self.BASE_URL
                + "/headlines/section/topic/{}".format(topic.upper())
                + self.__ceid()
            )

        else:
            d = self.__parse_feed(
                self.BASE_URL + "/topics/{}".format(topic) + self.__ceid(),
            )

        d["entries"] = self.__add_sub_articles(d["entries"])
        if len(d["entries"]) > 0:
            return d
        else:
            raise Exception("unsupported topic")

    def search(
        self,
        query: str,
        helper=True,
        when=None,
        from_=None,
        to_=None,
    ):
        """
        Return a list of all articles given a full-text search parameter,
        a country and a language

        :param bool helper: When True helps with URL quoting
        :param str when: Sets a time range for the artiles that can be found
        """

        if when:
            query += " when:" + when

        if from_ and not when:
            from_ = self.__from_to_helper(validate=from_)
            query += " after:" + from_

        if to_ and not when:
            to_ = self.__from_to_helper(validate=to_)
            query += " before:" + to_

        if helper:
            query = self.__search_helper(query)

        search_ceid = self.__ceid()
        search_ceid = search_ceid.replace("?", "&")

        d = self.__parse_feed(
            self.BASE_URL + "/search?q={}".format(query) + search_ceid,
        )

        d["entries"] = self.__add_sub_articles(d["entries"])
        return d
