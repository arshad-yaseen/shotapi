from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time


async def take_screenshot(
    url: str,
    width: int = None,
    height: int = None,
    full_page: bool = False,
    mobile: bool = False,
    dark_mode: bool = False,
    delay: int = 0,
    custom_js: str = None,
    user_agent: str = None,
) -> dict:
    options = Options()
    options.add_argument("--no-sandbox")

    if width and height:
        options.add_argument(f"--window-size={width},{height}")

    if mobile:
        options.add_argument("--window-size=375,812")  # iPhone X

    if dark_mode:
        options.add_argument("--force-dark-mode")

    if user_agent:
        options.add_argument(f"--user-agent={user_agent}")

    if full_page:
        options.add_argument("--start-fullscreen")

    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument("--hide-scrollbars")
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    try:
        driver.get(url)

        if delay > 0:
            time.sleep(delay)

        if custom_js:
            # Execute custom JavaScript on the page
            driver.execute_script(custom_js)

        # Full-page screenshot
        if full_page:
            total_width = driver.execute_script(
                "return document.body.offsetWidth"
            )
            total_height = driver.execute_script(
                "return document.body.parentNode.scrollHeight"
            )
            driver.set_window_size(total_width, total_height)

        screenshot_base64 = driver.get_screenshot_as_base64()
        screenshot_png = driver.get_screenshot_as_png()

        return {"base64": screenshot_base64, "png": screenshot_png}
    except Exception as e:
        raise e
    finally:
        if driver:
            driver.quit()
