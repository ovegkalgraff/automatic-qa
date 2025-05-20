# Automatic QA for TV 2 Play Smart TV Apps

This repository contains automated regression tests for TV 2 Play applications on different smart TV platforms.

## Supported Platforms

- Samsung TV: http://ctv.play.tv2.no/production/play/samsung
- LG TV: https://ctv.play.tv2.no/production/play/lg/
- Philips TV: https://ctv.play.tv2.no/production/play/philips/

## Project Structure

```
automatic-qa/
├── tests/                  # Test files directory
│   ├── test_samsung.py     # Tests for Samsung TV platform
│   ├── test_lg.py          # Tests for LG TV platform
│   ├── test_philips.py     # Tests for Philips TV platform
│   └── conftest.py         # Common test configuration
├── artifacts/              # Generated during test runs
│   ├── screenshots/        # Screenshots captured during tests
│   └── reports/            # Test reports in HTML format
├── run_tests.py            # Convenient test runner script
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/ovegkalgraff/automatic-qa.git
   cd automatic-qa
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Install Chrome/Chromium browser:
   - Chrome must be installed on your system
   - The webdriver-manager package will automatically download the appropriate ChromeDriver

## Running Tests

### Using the run_tests.py script

We've created a convenient wrapper script to run tests with different options:

```
# Run all tests
./run_tests.py

# Run tests for specific platforms
./run_tests.py --platforms samsung lg

# Run tests in parallel
./run_tests.py --parallel

# Run without HTML reports
./run_tests.py --no-html

# Run with minimal output
./run_tests.py --quiet
```

### Using pytest directly

```
# Run all tests
pytest

# Run tests for a specific platform
pytest tests/test_samsung.py  # Samsung TV tests
pytest tests/test_lg.py       # LG TV tests
pytest tests/test_philips.py  # Philips TV tests

# Run tests with HTML report
pytest --html=artifacts/reports/report.html

# Run tests in parallel
pytest -n 2  # Run with 2 parallel processes
```

## Test Features

The test suite includes:

1. **Basic Functionality Tests**
   - Page loading and element presence
   - Navigation and interaction

2. **Responsive Design Tests**
   - Testing at multiple resolutions
   - UI consistency across screen sizes

3. **Performance Tests**
   - Load time measurements
   - Resource usage

4. **Platform-Specific Features**
   - Testing unique aspects of each platform

## Test Configuration

The tests are configured using:

- `conftest.py` - Contains common fixtures and test configurations
- `pytest.ini` - Contains pytest configuration settings

## Adding New Tests

To add new tests:

1. Create a new test file in the `tests/` directory
2. Import the required modules and fixtures
3. Write test functions following the existing patterns
4. Use the common fixtures from `conftest.py` where applicable

Example:

```python
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def test_new_feature(chrome_driver):
    """Test a new feature of the TV app."""
    # Use the chrome_driver fixture
    driver = chrome_driver
    
    # Navigate to the app
    driver.get("https://ctv.play.tv2.no/production/play/samsung/")
    
    # Your test code
    # ...
```

## Screenshots

The test framework automatically takes screenshots in the following cases:

1. When tests fail (for debugging)
2. During responsive design tests (to verify appearance)
3. When explicitly called in tests using the `take_screenshot()` method

Screenshots are saved in the `artifacts/screenshots/` directory.

## HTML Reports

When running tests with the `--html` flag, detailed HTML reports are generated in the `artifacts/reports/` directory. These reports include:

- Test results summary
- Test execution details
- Environment information
- Error messages and tracebacks

## Troubleshooting

If you encounter issues:

1. **ChromeDriver issues**:
   - Ensure Chrome is installed and up to date
   - The webdriver-manager should handle driver installation automatically

2. **Test failures**:
   - Check screenshots in `artifacts/screenshots/`
   - Check the HTML report for detailed error messages
   - Verify network connectivity to test endpoints

3. **Environment issues**:
   - Ensure all dependencies are installed: `pip install -r requirements.txt`
   - Check that your Python version is compatible (3.6+)

## License

This project is licensed under the MIT License - see the LICENSE file for details.
