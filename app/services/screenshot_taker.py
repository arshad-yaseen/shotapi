from pyppeteer import launch

async def take_screenshot(url: str):
    try:
        browser = await launch()
        page = await browser.newPage()
        await page.goto(url)
        screenshot = await page.screenshot()
        return screenshot
    finally:
        await browser.close()
