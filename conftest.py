import pytest
from utils.browser_manager import BrowserManager


@pytest.fixture(scope="function")
def page(request):
    manager = BrowserManager(browser_type="chromium", headless=False)
    browser = manager.start_browser()

    context = browser.new_context()
    page = context.new_page()

    yield page

    # Screenshot on failure
    if request.node.rep_call.failed:
        page.screenshot(path=f"reports/{request.node.name}.png")

    context.close()
    manager.stop_browser()


# Hook to capture test result
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)