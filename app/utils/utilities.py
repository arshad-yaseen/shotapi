def format_time_remaining(seconds):
    """Format the remaining time in minutes and seconds."""
    mins, secs = divmod(seconds, 60)
    if mins:
        return f"{mins} minute(s) and {secs} second(s)"
    else:
        return f"{secs} second(s)"
