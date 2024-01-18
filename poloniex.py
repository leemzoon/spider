from playwright.sync_api import Playwright, sync_playwright, expect
import time
import os

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://support.poloniex.com/hc/zh-tw/sections/360006455114-%E6%9C%80%E6%96%B0%E5%85%AC%E5%91%8A")
    content = page.content()
    filename = 'log/page-{}.html'.format(time.strftime("%H"))
    with open(filename, 'w') as f:
        f.write(content)
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
