"""
headlinehunt Unit Testing
"""

import pytest

from headlinehunt.config import settings
from headlinehunt.main import Headliner


@pytest.fixture(scope="session", autouse=True)
def set_test_settings():
    settings.configure(FORCE_ENV_FOR_DYNACONF="testing")

@pytest.fixture(name="hh")
def Headliner_fixture():
    """return hh"""
    return Headliner()

@pytest.mark.asyncio
async def test_hh(hh):
    assert hh.news_feed is not None

