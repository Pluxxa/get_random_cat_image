import pytest
import requests
from unittest.mock import patch
from main import get_random_cat_image

# Тест успешного запроса
def test_get_random_cat_image_success(requests_mock):
    mock_url = "https://cdn2.thecatapi.com/images/abc123.jpg"
    requests_mock.get("https://api.thecatapi.com/v1/images/search", json=[{"url": mock_url}], status_code=200)

    result = get_random_cat_image()
    assert result == mock_url

# Тест неуспешного запроса (например, статус код 404)
def test_get_random_cat_image_failure(requests_mock):
    requests_mock.get("https://api.thecatapi.com/v1/images/search", status_code=404)

    result = get_random_cat_image()
    assert result is None
