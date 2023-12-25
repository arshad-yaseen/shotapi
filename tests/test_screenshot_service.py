from app.services.screenshot_service import validate_url


def test_validate_url_with_valid_url():
    assert validate_url("http://example.com") is True  # nosec


def test_validate_url_with_invalid_url():
    assert validate_url("not-a-valid-url") is False  # nosec
