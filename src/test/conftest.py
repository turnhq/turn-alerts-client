from datetime import datetime, timedelta
from typing import ByteString
import os

import pytest


@pytest.fixture
def internal_token():
    return os.environ.get("TOKEN")


@pytest.fixture
def host():
    return os.environ.get("HOST")
