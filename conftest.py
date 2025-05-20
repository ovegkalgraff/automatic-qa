#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Pytest configuration file for TV 2 Play Samsung app testing.
Contains fixtures and configuration for the test suite.
"""

import os
import pytest
import logging
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("tv2play_samsung_test.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

@pytest.fixture(scope="session")
def create_screenshots_dir():
    """Create a directory for storing screenshots if it doesn't exist."""
    screenshots_dir = "screenshots"
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)
    return screenshots_dir

@pytest.fixture(scope="class")
def chrome_driver():
    """Provides a configured Chrome WebDriver instance."""
    logger.info("Setting up Chrome WebDriver")

    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # For headless mode, uncomment the line below
    # chrome_options.add_argument("--headless")

    # Set user agent to simulate Samsung TV browser
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (SMART-TV; SAMSUNG; SmartTV; en) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.106 Safari/537.36")

    # Initialize the Chrome driver
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )

    driver.maximize_window()

    yield driver

    # Clean up after the test
    logger.info("Tearing down Chrome WebDriver")
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to take screenshots on test failures."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        # Get the driver from the test
        try:
            driver = item.instance.driver
            logger.info(f"Taking screenshot for failed test: {item.name}")

            # Create directory if it doesn't exist
            screenshots_dir = "screenshots"
            if not os.path.exists(screenshots_dir):
                os.makedirs(screenshots_dir)

            timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            screenshot_path = os.path.join(screenshots_dir, f"failure_{item.name}_{timestamp}.png")
            driver.save_screenshot(screenshot_path)
            logger.info(f"Screenshot saved to {screenshot_path}")
        except Exception as e:
            logger.error(f"Failed to capture screenshot on test failure: {e}")
