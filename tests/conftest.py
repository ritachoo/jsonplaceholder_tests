import pytest
from framework.jsonplaceholder_client import Client


@pytest.fixture
def client():
    return Client()
