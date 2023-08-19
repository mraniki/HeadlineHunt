"""
    

"""
import aiohttp

from headlinehunt.config import settings
from headlinehunt.provider import BaseProvider


class GNews(BaseProvider):
    """ """

    def __init__(self):
        super.__init__()
        self.news_url = settings.news_url
        # "https://gnews.io/api/v4/top-headlines?category=business&lang=en&max=2&apikey="

    async def fetch_top_news(self):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(self.news_url, timeout=10) as response:
                    data = await response.json()
                    articles = data.get("articles", [])
                    key_news = [
                        {"title": article["title"], "url": article["url"]}
                        for article in articles
                    ]
                    last_item = key_news[-1]
                    return f"📰 <a href='{last_item['url']}'>{last_item['title']}</a>"

        except aiohttp.ClientError as error:
            self.logger.warning("news %s", error)
            return None
