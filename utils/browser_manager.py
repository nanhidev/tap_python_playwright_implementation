from playwright.sync_api import sync_playwright

class BrowserManager:

    def __init__(self, browser_type="chromium", headless=False):
        self.browser_type = browser_type
        self.headless = headless
        self.playwright = None
        self.browser = None

    def start_browser(self):
        self.playwright = sync_playwright().start()

        if self.browser_type == "chromium":
            self.browser = self.playwright.chromium.launch(headless=self.headless)
        elif self.browser_type == "firefox":
            self.browser = self.playwright.firefox.launch(headless=self.headless)
        elif self.browser_type == "webkit":
            self.browser = self.playwright.webkit.launch(headless=self.headless)
        else:
            raise ValueError("Invalid browser type")

        return self.browser

    def stop_browser(self):
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()