import requests

API_URL = "http://localhost:8000/take"


def test_successful_screenshot_capture():
    response = requests.get(
        API_URL,
        params={"url": "http://example.com", "format": "base64"},
    )
    assert response.status_code == 200  # nosec
    assert isinstance(response.json(), str)  # nosec


def test_png_screenshot_capture():
    response = requests.get(
        API_URL,
        params={"url": "http://example.com", "format": "png"},
    )
    assert response.status_code == 200  # nosec
    assert response.headers["Content-Type"] == "image/png"  # nosec


def test_response_time():
    response = requests.get(
        API_URL,
        params={"url": "http://example.com", "format": "base64"},
        timeout=20,
    )
    assert response.elapsed.total_seconds() < 20  # nosec


def test_rate_limiting():
    # The rate limit is set at 10 requests per minute
    # Make 11 requests to test the rate limiting
    for _ in range(11):
        response = requests.get(
            API_URL,
            params={"url": "http://example.com", "format": "base64"},
        )

    # The last request should be rate limited
    assert response.status_code == 429  # nosec
    assert "Rate limit exceeded" in response.text  # nosec
