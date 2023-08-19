####
"""
    

"""

from newsplease import NewsPlease

from headlinehunt.config import settings
from headlinehunt.provider import BaseProvider


class NewsPlease(BaseProvider):
    """ """

    def __init__(self):
        super.__init__()

    async def get_news_url(self, url=None):
        return NewsPlease.from_url(url).title
