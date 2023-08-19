"""
    

"""
import finnhub

from headlinehunt.config import settings
from headlinehunt.provider import BaseProvider


class FinnHub(BaseProvider):
    """ """

    def __init__(self):
        super.__init__()
        self.client = finnhub.Client(api_key=settings.finnhub_api_key)

    async def get_news_topic(self, topic="forex"):
        return self.client.general_news(topic, min_id=0)

    async def fetch_sentiment(self, symbol="AAPL"):
        return self.client.news_sentiment(symbol)
