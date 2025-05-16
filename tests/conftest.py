import pytest
import os
import json
from datetime import datetime
from pathlib import Path

# Create directories for test artifacts
@pytest.fixture(scope="session", autouse=True)
def setup_test_environment():
    """Set up the test environment before any tests run."""
    # Create directories for artifacts
    artifacts_dir = Path("artifacts")
    screenshots_dir = artifacts_dir / "screenshots"
    reports_dir = artifacts_dir / "reports"
    
    for directory in [artifacts_dir, screenshots_dir, reports_dir]:
        directory.mkdir(exist_ok=True)
    
    # Set up session timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    return {
        "timestamp": timestamp,
        "artifacts_dir": str(artifacts_dir),
        "screenshots_dir": str(screenshots_dir),
        "reports_dir": str(reports_dir)
    }

# Add a hook for better test reporting
def pytest_runtest_makereport(item, call):
    if "driver" in item.funcargs:
        driver = item.funcargs["driver"]
        nodeid = item.nodeid
        
        if call.when == "call":
            # Take a screenshot on test failure
            if call.excinfo is not None:
                try:
                    # Create a sanitized test name for the filename
                    test_name = nodeid.replace("::", "_").replace("/", "_").replace(".", "_")
                    screenshot_path = f"artifacts/screenshots/fail_{test_name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
                    
                    driver.save_screenshot(screenshot_path)
                    print(f"Screenshot saved to {screenshot_path}")
                except Exception as e:
                    print(f"Failed to take screenshot: {e}")

# Custom logger fixture
@pytest.fixture
def logger(request):
    """Fixture for test logging."""
    test_name = request.node.name
    
    def _log_info(message):
        """Log an info message with the test name."""
        print(f"[INFO] [{test_name}] {message}")
    
    def _log_error(message):
        """Log an error message with the test name."""
        print(f"[ERROR] [{test_name}] {message}")
    
    def _log_warning(message):
        """Log a warning message with the test name."""
        print(f"[WARNING] [{test_name}] {message}")
    
    class Logger:
        def info(self, message):
            _log_info(message)
        
        def error(self, message):
            _log_error(message)
        
        def warning(self, message):
            _log_warning(message)
    
    return Logger() 