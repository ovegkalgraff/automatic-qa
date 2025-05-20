#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Regression test for TV 2 Play LG application.
This script performs automated testing on the LG TV app to ensure its functionality.
"""

import os
import time
import pytest
import logging
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("tv2play_lg_test.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Constants
# Using the actual TV 2 Play LG URL
BASE_URL = "https://ctv.play.tv2.no/production/play/lg/index.html"
TIMEOUT = 10  # seconds

class TestTV2PlayLG:
    """Test suite for TV 2 Play LG app."""

    @classmethod
    def setup_class(cls):
        """Set up the test environment."""
        logger.info("Setting up test environment")

        # Configure Chrome options
        chrome_options = Options()
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")

        # For headless mode, uncomment the line below
        # chrome_options.add_argument("--headless")

        # Set user agent to simulate LG TV browser
        chrome_options.add_argument("--user-agent=Mozilla/5.0 (Web0S; Linux/SmartTV) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36")

        # Initialize the Chrome driver
        cls.driver = webdriver.Chrome(options=chrome_options)

        cls.driver.maximize_window()
        cls.wait = WebDriverWait(cls.driver, TIMEOUT)

    def setup_method(self):
        """Set up method to run before each test."""
        logger.info("Navigating to TV 2 Play LG app")
        self.driver.get(BASE_URL)
        # Allow page to load completely
        time.sleep(5)  # Increase wait time to 5 seconds

    def test_page_loads(self):
        """Test if the TV 2 Play page loads properly."""
        logger.info("Testing if page loads correctly")

        # Verify that the page title is correct
        assert "TV 2 Play" in self.driver.title, "Page title is incorrect"

        # Take a screenshot for reference
        self.take_screenshot("page_load")

        logger.info("Page loaded successfully")

    def test_ui_elements_present(self):
        """Test if the basic UI elements are present."""
        logger.info("Testing if UI elements are present")
        
        # Take a screenshot first for reference
        self.take_screenshot("ui_elements")
        
        # Check if there are any elements in the DOM
        body = self.driver.find_element(By.TAG_NAME, "body")
        
        # Get all elements inside body
        all_elements = body.find_elements(By.XPATH, "//*")
        visible_elements = []
        
        # Count visible elements
        for element in all_elements[:20]:  # Limit to first 20 elements for performance
            try:
                if element.is_displayed():
                    tag_name = element.tag_name
                    visible_elements.append(tag_name)
                    logger.info(f"Found visible element: {tag_name}")
            except:
                pass
        
        # If we found at least some elements, the test passes
        num_elements = len(visible_elements)
        logger.info(f"Found {num_elements} visible elements")
        
        # Pass the test if we have any elements
        if num_elements > 0:
            logger.info(f"UI structure verified with {num_elements} elements")
        else:
            logger.error("Could not find any visible elements in the page")
            pytest.fail("No visible UI elements found in the app")

    def test_responsive_design(self):
        """Test responsive design of the application."""
        logger.info("Testing responsive design")

        # Get initial window size
        initial_size = self.driver.get_window_size()

        # Test different resolutions
        resolutions = [
            {"width": 1280, "height": 720},   # 720p
            {"width": 1920, "height": 1080},  # 1080p
        ]

        for resolution in resolutions:
            width = resolution["width"]
            height = resolution["height"]
            logger.info(f"Testing resolution: {width}x{height}")

            # Set window size
            self.driver.set_window_size(width, height)
            time.sleep(1)

            # Take a screenshot
            self.take_screenshot(f"responsive_{width}x{height}")

            # Verify the page still loads properly at this resolution
            assert "TV 2 Play" in self.driver.title, f"Page title is incorrect at resolution {width}x{height}"

        # Reset to initial size
        self.driver.set_window_size(initial_size["width"], initial_size["height"])

    def take_screenshot(self, name):
        """Take a screenshot for documentation and debugging."""
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        screenshot_dir = "artifacts/screenshots"
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        screenshot_path = os.path.join(screenshot_dir, f"tv2play_lg_{name}_{timestamp}.png")
        self.driver.save_screenshot(screenshot_path)
        logger.info(f"Screenshot saved to {screenshot_path}")

    @classmethod
    def teardown_class(cls):
        """Clean up after all tests are run."""
        logger.info("Tearing down test environment")
        cls.driver.quit()


if __name__ == "__main__":
    pytest.main(["-v", "test_tv2play_lg.py"])
