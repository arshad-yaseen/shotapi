from pyppeteer import launch


async def take_screenshot(url: str):
    browser = None
    try:
        browser = await launch(
            headless=True,
            args=[
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--disable-gpu",
                "--disable-software-rasterizer",
                "--disable-setuid-sandbox",
            ],
        )
        page = await browser.newPage()
        await page.goto(url)
        screenshot = await page.screenshot()
        return screenshot
    except Exception as e:
        raise e
    finally:
        if browser:
            await browser.close()
