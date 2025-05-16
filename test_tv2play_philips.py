#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Regression test for TV 2 Play Philips application.
This script performs automated testing on the Philips TV app to ensure its functionality.
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
                logging.FileHandler("tv2play_philips_test.log"),
                logging.StreamHandler()
      ]
)

logger = logging.getLogger(__name__)

# Philips TV app URL
PHILIPS_APP_URL = "https://ctv.play.tv2.no/production/play/philips/"

class TestTV2PlayPhilipsApp:
      """Test suite for TV 2 Play Philips app."""

    def test_page_load(self, driver):
              """Test that the Philips app page loads successfully."""
              logger.info("Testing Philips app page load")
              try:
                            driver.get(PHILIPS_APP_URL)

            # Wait for the page to load
                  WebDriverWait(driver, 10).until(
                                    EC.presence_of_element_located((By.TAG_NAME, "body"))
                  )

            logger.info("Philips app page loaded successfully")

            # Take screenshot of loaded page
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = os.path.join("screenshots", f"philips_app_loaded_{timestamp}.png")
            os.makedirs(os.path.dirname(screenshot_path), exist_ok=True)
            driver.save_screenshot(screenshot_path)
            logger.info(f"Screenshot saved to {screenshot_path}")

            # Verify title
            assert "TV 2 Play" in driver.title, f"Unexpected page title: {driver.title}"

            # Check if there are any console errors
            logs = driver.get_log('browser')
            severe_logs = [log for log in logs if log['level'] == 'SEVERE']
            assert len(severe_logs) == 0, f"Found {len(severe_logs)} severe errors in console"

except TimeoutException:
            logger.error("Timeout waiting for Philips app page to load")
            driver.save_screenshot("screenshots/philips_app_load_timeout.png")
            pytest.fail("Timeout waiting for Philips app page to load")
except Exception as e:
            logger.error(f"Error loading Philips app page: {str(e)}")
            driver.save_screenshot("screenshots/philips_app_load_error.png")
            pytest.fail(f"Error loading Philips app page: {str(e)}")

    def test_ui_elements(self, driver):
              """Test that UI elements are present and functioning."""
        logger.info("Testing Philips app UI elements")
        try:
                      driver.get(PHILIPS_APP_URL)

            # Wait for the page to load
                      WebDriverWait(driver, 10).until(
                          EC.presence_of_element_located((By.TAG_NAME, "body"))
                      )

            # Check for logo or main elements (adjust selectors based on actual app structure)
                      # Since we don't have specific knowledge about the page structure, we'll use
                      # generic selectors for testing purposes. These should be updated with actual selectors.
                      try:
                                        # Look for img elements
                                        WebDriverWait(driver, 5).until(
                                                              EC.presence_of_element_located((By.TAG_NAME, "img"))
                                        )
                                        images = driver.find_elements(By.TAG_NAME, "img")
                                        assert len(images) > 0, "No images found on the page"
                                        logger.info(f"Found {len(images)} images on the page")

                # Check for specific UI components common in TV apps
                          content_elements = driver.find_elements(By.TAG_NAME, "div")
                assert len(content_elements) > 0, "No content elements found"
                logger.info(f"Found {len(content_elements)} div elements")

                # Take screenshot of UI elements
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                screenshot_path = os.path.join("screenshots", f"philips_app_ui_{timestamp}.png")
                driver.save_screenshot(screenshot_path)
                logger.info(f"UI elements screenshot saved to {screenshot_path}")

except TimeoutException:
                logger.warning("Some UI elements not found within timeout")
                driver.save_screenshot("screenshots/philips_app_ui_timeout.png")

except Exception as e:
            logger.error(f"Error testing UI elements: {str(e)}")
            driver.save_screenshot("screenshots/philips_app_ui_error.png")
            pytest.fail(f"Error testing UI elements: {str(e)}")

    def test_responsive_design(self, driver):
              """Test that the app responds appropriately to different screen sizes."""
              logger.info("Testing Philips app responsive design")

        # Common TV resolutions to test
              resolutions = [
                            (1280, 720),  # HD
                            (1920, 1080), # Full HD
                            (3840, 2160)  # 4K UHD
              ]

        try:
                      for width, height in resolutions:
                                        logger.info(f"Testing resolution: {width}x{height}")
                                        driver.set_window_size(width, height)
                                        time.sleep(1)  # Allow time for responsive adjustments

                driver.get(PHILIPS_APP_URL)
                WebDriverWait(driver, 10).until(
                                      EC.presence_of_element_located((By.TAG_NAME, "body"))
                )

                # Take screenshot at this resolution
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                screenshot_path = os.path.join(
                                      "screenshots", 
                                      f"philips_app_{width}x{height}_{timestamp}.png"
                )
                driver.save_screenshot(screenshot_path)
                logger.info(f"Screenshot at {width}x{height} saved to {screenshot_path}")

                # Check visibility of main elements
                body = driver.find_element(By.TAG_NAME, "body")
                assert body.is_displayed(), "Body not visible at this resolution"

                # Look for potential overflow issues (scrollbars)
                # This is a simplified check - real testing would be more comprehensive
                has_horizontal_scrollbar = driver.execute_script(
                                      "return document.documentElement.scrollWidth > document.documentElement.clientWidth"
                )
                logger.info(f"Horizontal scrollbar present: {has_horizontal_scrollbar}")
                # On TV apps, horizontal scrolling is often intentional, so we just log it
                # rather than asserting against it

except Exception as e:
            logger.error(f"Error testing responsive design: {str(e)}")
            driver.save_screenshot("screenshots/philips_app_responsive_error.png")
            pytest.fail(f"Error testing responsive design: {str(e)}")

    def test_navigation_simulation(self, driver):
              """Simulate remote control navigation in the Philips TV app interface."""
              logger.info("Testing navigation simulation in Philips app")
              try:
                            driver.get(PHILIPS_APP_URL)
                            WebDriverWait(driver, 10).until(
                                EC.presence_of_element_located((By.TAG_NAME, "body"))
                            )

            # Take baseline screenshot
                  driver.save_screenshot("screenshots/philips_app_navigation_start.png")

            # Simulate remote control navigation using keyboard
            # Arrow keys are commonly used for TV navigation
            body = driver.find_element(By.TAG_NAME, "body")

            # Send arrow key events to simulate remote navigation
            # Down
            body.send_keys(webdriver.Keys.ARROW_DOWN)
            time.sleep(0.5)
            driver.save_screenshot("screenshots/philips_app_nav_down.png")

            # Right
            body.send_keys(webdriver.Keys.ARROW_RIGHT)
            time.sleep(0.5)
            driver.save_screenshot("screenshots/philips_app_nav_right.png")

            # Up
            body.send_keys(webdriver.Keys.ARROW_UP)
            time.sleep(0.5)
            driver.save_screenshot("screenshots/philips_app_nav_up.png")

            # Left
            body.send_keys(webdriver.Keys.ARROW_LEFT)
            time.sleep(0.5)
            driver.save_screenshot("screenshots/philips_app_nav_left.png")

            # Enter/Select (simulating OK button on remote)
            body.send_keys(webdriver.Keys.ENTER)
            time.sleep(1)
            driver.save_screenshot("screenshots/philips_app_nav_enter.png")

            logger.info("Navigation simulation completed")

except Exception as e:
            logger.error(f"Error during navigation simulation: {str(e)}")
            driver.save_screenshot("screenshots/philips_app_navigation_error.png")
            pytest.fail(f"Error during navigation simulation: {str(e)}")

    def test_performance_metrics(self, driver):
              """Measure and log basic performance metrics."""
              logger.info("Testing Philips app performance metrics")
              try:
                            # Measure page load time
                            start_time = time.time()
                            driver.get(PHILIPS_APP_URL)
                            WebDriverWait(driver, 20).until(
                                EC.presence_of_element_located((By.TAG_NAME, "body"))
                            )
                            end_time = time.time()
                            load_time = end_time - start_time

            logger.info(f"Page load time: {load_time:.2f} seconds")

            # Get console logs
            logs = driver.get_log('browser')

            # Calculate metrics
            error_count = len([log for log in logs if log['level'] in ('SEVERE', 'ERROR')])
            warning_count = len([log for log in logs if log['level'] == 'WARNING'])

            # Log summary
            logger.info(f"Performance Summary:")
            logger.info(f"- Load Time: {load_time:.2f} seconds")
            logger.info(f"- Console Errors: {error_count}")
            logger.info(f"- Console Warnings: {warning_count}")

            # Check against reasonable thresholds
            assert load_time < 10, f"Page load time of {load_time:.2f}s exceeds 10s threshold"
            assert error_count == 0, f"Found {error_count} console errors"

            # Take final screenshot
            driver.save_screenshot("screenshots/philips_app_performance.png")

except Exception as e:
            logger.error(f"Error during performance testing: {str(e)}")
            driver.save_screenshot("screenshots/philips_app_performance_error.png")
            pytest.fail(f"Error during performance testing: {str(e)}")

    def test_philips_specific_features(self, driver):
              """Test Philips TV-specific features and interactions."""
              logger.info("Testing Philips-specific features")
              try:
                            driver.get(PHILIPS_APP_URL)
                            WebDriverWait(driver, 10).until(
                                EC.presence_of_element_located((By.TAG_NAME, "body"))
                            )

            # Check for Philips-specific UI elements or behaviors
                  # This is a placeholder - actual Philips-specific tests would depend on
            # unique features in the Philips TV app implementation

            # Example: Check for Ambilight-related features (if implemented in web app)
            # This is just a placeholder example
            try:
                              # Look for elements with ambilight-related class or ID
                              ambilight_elements = driver.find_elements(By.CSS_SELECTOR, "[class*='ambilight'], [id*='ambilight']")
                              if ambilight_elements:
                                                    logger.info(f"Found {len(ambilight_elements)} ambilight-related elements")
            else:
                    logger.info("No ambilight-related elements found")
            except Exception as e:
                logger.warning(f"Error checking for Philips-specific features: {str(e)}")

            # Example: Check for Philips remote control compatibility
            # Test interactions that would be specific to Philips remote controls

            # Take screenshot of Philips-specific features
            driver.save_screenshot("screenshots/philips_specific_features.png")

except Exception as e:
            logger.error(f"Error testing Philips-specific features: {str(e)}")
            driver.save_screenshot("screenshots/philips_specific_features_error.png")
            pytest.fail(f"Error testing Philips-specific features: {str(e)}")
