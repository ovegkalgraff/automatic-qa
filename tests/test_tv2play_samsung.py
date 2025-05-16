#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Regression test for TV 2 Play Samsung application.
This script performs automated testing on the Samsung TV app to ensure its functionality.
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
                logging.FileHandler("tv2play_samsung_test.log"),
                logging.StreamHandler()
      ]
)

logger = logging.getLogger(__name__)

# Constants
BASE_URL = "https://ctv.play.tv2.no/production/play/samsung/index.html"
TIMEOUT = 10  # seconds

class TestTV2PlaySamsung:
      """Test suite for TV 2 Play Samsung app."""

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

        # Set user agent to simulate Samsung TV browser
              chrome_options.add_argument("--user-agent=Mozilla/5.0 (SMART-TV; SAMSUNG; SmartTV; en) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.106 Safari/537.36")

        # Initialize the Chrome driver
              cls.driver = webdriver.Chrome(
                  service=Service(ChromeDriverManager().install()),
                  options=chrome_options
              )

        cls.driver.maximize_window()
        cls.wait = WebDriverWait(cls.driver, TIMEOUT)

    def setup_method(self):
              """Set up method to run before each test."""
              logger.info("Navigating to TV 2 Play Samsung app")
              self.driver.get(BASE_URL)
              # Allow page to load completely
              time.sleep(3)

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

        # Check for the TV 2 Play logo
              try:
                            logo = self.wait.until(
                                              EC.presence_of_element_located((By.XPATH, "//img[contains(@src, 'logo')]"))
                            )
                            assert logo.is_displayed(), "Logo is not displayed"
                            logger.info("Logo is displayed")
except (TimeoutException, NoSuchElementException) as e:
            logger.error(f"Error finding logo: {e}")
            self.take_screenshot("logo_error")
            pytest.fail("Could not find logo element")

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
              screenshot_dir = "screenshots"
              if not os.path.exists(screenshot_dir):
                            os.makedirs(screenshot_dir)

              screenshot_path = os.path.join(screenshot_dir, f"{name}_{timestamp}.png")
              self.driver.save_screenshot(screenshot_path)
              logger.info(f"Screenshot saved to {screenshot_path}")

    @classmethod
    def teardown_class(cls):
              """Clean up after all tests are run."""
              logger.info("Tearing down test environment")
              cls.driver.quit()


if __name__ == "__main__":
      pytest.main(["-v", "test_tv2play_samsung.py"])
