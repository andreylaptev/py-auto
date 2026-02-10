# Web Test Automation Framework (Python + Playwright)

A test automation framework for web applications using **Python**, **pytest**, and **Playwright**.

## Project structure

```
py-auto/
├── config/              # Configuration and settings
│   ├── __init__.py
│   └── settings.py
├── pages/               # Page Object Model
│   ├── __init__.py
│   ├── base_page.py
│   └── example_page.py
├── tests/               # Test suites
│   ├── conftest.py      # Pytest and Playwright fixtures
│   └── e2e/             # End-to-end tests
│       └── test_example.py
├── utils/               # Helpers and utilities
│   ├── __init__.py
│   └── helpers.py
├── reports/             # Test reports and screenshots (generated)
├── .env.example         # Environment variables template
├── pyproject.toml
├── pytest.ini
├── requirements.txt
└── README.md
```

## Setup

1. **Create a virtual environment** (recommended):

   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # Windows
   # source .venv/bin/activate   # Linux/macOS
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   # or: pip install -e .
   ```

3. **Install Playwright browsers** (one-time; the Python package is in `requirements.txt`, this step downloads the browser binaries):

   ```bash
   playwright install
   ```

4. **Configure environment**:

   ```bash
   copy .env.example .env   # Windows
   # cp .env.example .env   # Linux/macOS
   ```

   Edit `.env` and set `BASE_URL` to your application URL.

## Running tests

- Run all tests:
  ```bash
  pytest
  ```

- Run with UI:
  ```bash
  pytest --headed
  ```

- Run only E2E / smoke:
  ```bash
  pytest -m e2e
  pytest -m smoke
  ```

- Run a specific file or test:
  ```bash
  pytest tests/e2e/test_example.py
  pytest tests/e2e/test_example.py::test_example_page_loads
  ```

- Generate HTML report (with optional dependency):
  ```bash
  pip install pytest-html
  pytest --html=reports/report.html
  ```

- Parallel runs (optional):
  ```bash
  pip install pytest-xdist
  pytest -n auto
  ```

## Configuration

| Variable          | Description              | Default        |
|-------------------|--------------------------|----------------|
| `BASE_URL`        | Application under test   | `https://example.com` |
| `BROWSER`         | `chromium`, `firefox`, `webkit` | `chromium` |
| `HEADED`          | Run browser visible      | `false`       |
| `SLOW_MO`         | Delay in ms              | `0`           |
| `DEFAULT_TIMEOUT` | Timeout in ms            | `30000`       |

## Writing tests

- Put **page objects** in `pages/` (inherit from `BasePage`).
- Put **E2E tests** in `tests/e2e/` and use the `page` fixture.
- Use markers: `@pytest.mark.e2e`, `@pytest.mark.smoke`.
- Screenshots on failure are saved under `reports/screenshots/`.

## References

- [Playwright for Python](https://playwright.dev/python/)
- [pytest-playwright](https://pytest-playwright.readthedocs.io/)
