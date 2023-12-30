from limits import RateLimitItemPerMinute
from limits.strategies import MovingWindowRateLimiter
from limits.storage import MemoryStorage
from datetime import datetime, timedelta
from app.utils.utilities import format_time_remaining
from fastapi import HTTPException

storage = MemoryStorage()
limiter = MovingWindowRateLimiter(storage)


def check_rate_limit(client_ip: str, rate_per_minute: int):
    if not limiter.hit(RateLimitItemPerMinute(rate_per_minute), client_ip):
        reset_time = datetime.now() + timedelta(
            minutes=1
        )  # Assuming a 1-minute window
        time_remaining = (reset_time - datetime.now()).total_seconds()
        formatted_time = format_time_remaining(time_remaining)
        detail = f"Rate limit exceeded. Please try again in {formatted_time}."
        raise HTTPException(status_code=429, detail=detail)
