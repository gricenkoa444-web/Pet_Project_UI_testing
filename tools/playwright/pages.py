from contextlib import contextmanager

import allure
from playwright.sync_api import Playwright, Page

from config import settings, Browser
from tools.playwright.mocks import mock_static_resources


@contextmanager
def initialize_playwright_page(
        playwright: Playwright,
        test_name: str,
        browser_type: Browser,
        storage_state: str | None = None
) -> Page:
    browser = playwright[browser_type].launch(headless=settings.headless)
    context = browser.new_context(
        base_url=settings.app_url.unicode_string(),
        storage_state=storage_state,
        record_video_dir=settings.videos_dir
    )
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    mock_static_resources(page)
    try:
        yield page
    finally:
        trace_path = settings.tracing_dir.joinpath(f'{test_name}.zip')
        context.tracing.stop(path=trace_path)

        browser.close()

        if trace_path.exists():
            allure.attach.file(trace_path, name='trace', extension='zip')

        if page.video and page.video.path():
            allure.attach.file(page.video.path(), name='video', attachment_type=allure.attachment_type.WEBM)