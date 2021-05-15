# TODO(everyone): 웹서버의 healthz가 response code 200 확인

import pytest
import requests
import os
import sys
sys.path.append(
    os.path.dirname(os.path.dirname(__file__))
)
from app import create_app

@pytest.fixture
def api():
    app = create_app()
    return app.test_client()


def test_health_check():
    response = requests.get(url="http://localhost:8080/healthz")
    assert response.status_code == 200