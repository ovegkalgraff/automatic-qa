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
│   └── reports/            # Test reports
├── requirements.txt        # Python dependencies
└── README.md               # This file
```

## Setup

1. Clone this repository:
   ```
   git clone https://github.com/ovegkalgraff/automatic-qa.git
   cd automatic-qa
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Install Chrome/Chromium browser and corresponding WebDriver.

## Running Tests

### Run all tests
```
pytest
```

### Run tests for a specific platform
```
pytest tests/test_samsung.py  # Samsung TV tests
pytest tests/test_lg.py       # LG TV tests
pytest tests/test_philips.py  # Philips TV tests
```

### Run tests with HTML report
```
pytest --html=report.html
```

### Run tests in parallel
```
pytest -n 3  # Run with 3 parallel processes
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

## Adding New Tests

To add a new test:

1. Create a new test file in the `tests/` directory
2. Import the required modules and fixtures
3. Write test functions following the existing patterns
4. Use the common fixtures from `conftest.py` where applicable

## CI/CD Integration

This test suite can be integrated with CI/CD pipelines to run tests automatically on code changes.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
