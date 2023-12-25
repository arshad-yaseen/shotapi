import requests

API_URL = "http://localhost:8000/"


def test_successful_screenshot_capture():
    response = requests.post(
        API_URL, json={"url": "http://example.com"}, timeout=10
    )
    assert response.status_code == 200  # nosec
    assert isinstance(response.json(), str)  # nosec


def test_asking_for_cloudinary_screenshot_without_credentials():
    response = requests.post(
        API_URL,
        json={"url": "http://example.com", "type": "cloudinary"},
        timeout=10,
    )
    assert response.status_code == 422  # nosec


def test_response_time():
    response = requests.post(
        API_URL, json={"url": "http://example.com"}, timeout=10
    )
    assert response.elapsed.total_seconds() < 10  # nosec
