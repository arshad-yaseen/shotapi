from selenium import webdriver
from selenium.webdriver.chrome.options import Options

async def take_screenshot(url: str):
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_argument('--window-size=1280,800')
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')

    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get(url)
        screenshot_base64 = driver.get_screenshot_as_base64()
        return screenshot_base64
    except Exception as e:
        raise e
    finally:
        if driver:
            driver.quit()
