import requests

API_URL = "http://localhost:8000/"


def test_successful_screenshot_capture():
    response = requests.post(
        API_URL, json={"url": "http://example.com"}, timeout=20
    )
    assert response.status_code == 200  # nosec
    assert isinstance(response.json(), str)  # nosec


def test_asking_for_cloudinary_screenshot_without_credentials():
    response = requests.post(
        API_URL,
        json={"url": "http://example.com", "format": "cloudinary_url"},
        timeout=20,
    )
    assert response.status_code == 422  # nosec


def test_response_time():
    response = requests.post(
        API_URL, json={"url": "http://example.com"}, timeout=20
    )
    assert response.elapsed.total_seconds() < 20  # nosec


def test_rate_limiting():
    # The rate limit is set at 6 requests per minute
    # Make 7 requests to test the rate limiting
    for _ in range(7):
        response = requests.post(API_URL, json={"url": "http://example.com"})

    # The last request should be rate limited
    assert response.status_code == 429  # nosec
    assert "Rate limit exceeded" in response.text  # nosec
