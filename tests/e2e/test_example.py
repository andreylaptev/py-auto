"""Example E2E tests - replace with your application tests."""

import pytest

from pages.example_page import ExamplePage


@pytest.mark.e2e
@pytest.mark.smoke
def test_example_page_loads(page, base_url):
    """Example: verify page loads and has expected structure."""
    example_page = ExamplePage(page)
    example_page.navigate()
    example_page.wait_for_load_state("networkidle")
    assert page.url.startswith(base_url)


@pytest.mark.e2e
def test_example_navigation(page):
    """Example: navigate and check title (adapt to your app)."""
    example_page = ExamplePage(page)
    example_page.navigate()
    title = example_page.get_title()
    assert title is not None
    assert len(title) > 0
