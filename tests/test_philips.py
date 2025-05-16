import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# Philips TV app URL
PHILIPS_APP_URL = "https://ctv.play.tv2.no/production/play/philips/"

# Different screen resolutions to test
RESOLUTIONS = [
    (1920, 1080),  # Full HD
    (3840, 2160),  # 4K UHD
    (1280, 720)    # HD
]

@pytest.fixture
def driver():
    """Set up WebDriver for Philips TV tests."""
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--user-agent=Mozilla/5.0 (SMART-TV; PHILIPS-OS) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(30)
    
    yield driver
    
    driver.quit()

def test_philips_app_loads(driver):
    """Test that the Philips TV app loads successfully."""
    driver.get(PHILIPS_APP_URL)
    
    # Wait for the app to load
    try:
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".app-container, #app, .tv-app"))
        )
        assert "TV 2 Play" in driver.title
        print("Philips TV app loaded successfully")
    except TimeoutException:
        pytest.fail("Philips TV app failed to load within the timeout period")

def test_responsive_design(driver):
    """Test the app's responsive design across different screen resolutions."""
    for width, height in RESOLUTIONS:
        driver.set_window_size(width, height)
        driver.get(PHILIPS_APP_URL)
        
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".app-container, #app, .tv-app"))
            )
            # Take screenshot for visual verification
            driver.save_screenshot(f"philips_resolution_{width}x{height}.png")
            
            # Check if the layout adjusts properly
            viewport_width = driver.execute_script("return window.innerWidth")
            viewport_height = driver.execute_script("return window.innerHeight")
            
            assert abs(viewport_width - width) <= 10
            assert abs(viewport_height - height) <= 10
            
            print(f"Responsive design works for resolution {width}x{height}")
        except (TimeoutException, AssertionError) as e:
            pytest.fail(f"Responsive design test failed for resolution {width}x{height}: {str(e)}")

def test_navigation(driver):
    """Test navigation through the Philips TV app."""
    driver.get(PHILIPS_APP_URL)
    
    # Wait for the app to load
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".app-container, #app, .tv-app"))
    )
    
    # Navigation elements can vary, so we'll check for common navigation elements
    try:
        # Check for navigation menu
        navigation = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "nav, .navigation, .menu, .sidebar"))
        )
        assert navigation.is_displayed(), "Navigation menu is not displayed"
        
        # Look for menu items/buttons
        menu_items = driver.find_elements(By.CSS_SELECTOR, "nav a, .navigation a, .menu-item, .nav-item")
        assert len(menu_items) > 0, "No navigation menu items found"
        
        # Try clicking on the first menu item if it exists
        if len(menu_items) > 0:
            first_item = menu_items[0]
            first_item_text = first_item.text
            first_item.click()
            
            # Wait for page to update after navigation
            time.sleep(2)
            
            # Verify navigation happened (URL changed or new elements appeared)
            current_url = driver.current_url
            assert current_url != PHILIPS_APP_URL or driver.find_elements(By.CSS_SELECTOR, ".content-changed, .new-view"), \
                "Navigation did not appear to work"
            
            print(f"Successfully navigated to {first_item_text}")
    except (TimeoutException, NoSuchElementException, AssertionError) as e:
        pytest.fail(f"Navigation test failed: {str(e)}")

def test_performance_metrics(driver):
    """Test performance metrics of the Philips TV app."""
    driver.get(PHILIPS_APP_URL)
    
    # Measure load time
    start_time = time.time()
    
    try:
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".app-container, #app, .tv-app"))
        )
        load_time = time.time() - start_time
        
        # Log performance data
        print(f"Page load time: {load_time:.2f} seconds")
        
        # Execute JavaScript to get performance metrics
        navigation_timing = driver.execute_script("""
            var performance = window.performance || {};
            var timings = performance.timing || {};
            return {
                navigationStart: timings.navigationStart,
                responseEnd: timings.responseEnd,
                domComplete: timings.domComplete,
                loadEventEnd: timings.loadEventEnd
            };
        """)
        
        if navigation_timing['navigationStart']:
            dns_time = (navigation_timing['responseEnd'] - navigation_timing['navigationStart']) / 1000
            dom_load_time = (navigation_timing['domComplete'] - navigation_timing['navigationStart']) / 1000
            page_load_time = (navigation_timing['loadEventEnd'] - navigation_timing['navigationStart']) / 1000
            
            print(f"DNS Time: {dns_time:.2f} seconds")
            print(f"DOM Load Time: {dom_load_time:.2f} seconds")
            print(f"Total Page Load Time: {page_load_time:.2f} seconds")
            
            # Assert reasonable performance
            assert page_load_time < 10, f"Page load time ({page_load_time:.2f}s) exceeds threshold of 10s"
    except (TimeoutException, AssertionError) as e:
        pytest.fail(f"Performance test failed: {str(e)}")

def test_philips_specific_features(driver):
    """Test Philips TV specific features and optimizations."""
    driver.get(PHILIPS_APP_URL)
    
    # Wait for the app to load
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".app-container, #app, .tv-app"))
    )
    
    try:
        # Check for Philips-specific UI elements or attributes
        philips_elements = driver.find_elements(By.CSS_SELECTOR, "[data-platform='philips'], .philips-feature, .philips-specific")
        
        # If specific Philips elements exist, verify they're working
        if len(philips_elements) > 0:
            for element in philips_elements:
                assert element.is_displayed(), f"Philips-specific element {element.get_attribute('class')} is not displayed"
            print(f"Found {len(philips_elements)} Philips-specific elements")
        
        # Check if the app is optimized for remote control navigation
        # (Focus state is important for TV apps)
        focused_elements = driver.find_elements(By.CSS_SELECTOR, ":focus, .focused, [data-focused='true']")
        if len(focused_elements) > 0:
            assert focused_elements[0].is_displayed(), "Focused element is not visible"
            print("Focus management is working")
        
        # Check for video playback capability
        video_elements = driver.find_elements(By.TAG_NAME, "video")
        if len(video_elements) > 0:
            # If video element exists, check if it can be interacted with
            video = video_elements[0]
            driver.execute_script("arguments[0].play()", video)
            time.sleep(2)
            is_playing = driver.execute_script("return !arguments[0].paused", video)
            assert is_playing, "Video failed to play"
            print("Video playback is functional")
            
    except (NoSuchElementException, AssertionError) as e:
        pytest.fail(f"Philips-specific features test failed: {str(e)}") 