"""
    

"""

from headlinehunt.config import settings
from headlinehunt.provider import BaseProvider


class AlphaVantage(BaseProvider):
    """ """

    def __init__(self):
        super.__init__()
        self.client = None
