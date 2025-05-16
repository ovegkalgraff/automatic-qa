# Automatic QA

Repository for automated quality assurance tools and scripts.

## TV 2 Play Samsung App Regression Test

This repository contains automated regression tests for the TV 2 Play Samsung app. The tests verify that:
1. The page loads correctly
2. 2. UI elements are present and functional
   3. 3. The application responds appropriately to different screen resolutions
     
      4. ### Prerequisites
     
      5. - Python 3.8 or higher
         - - Chrome browser installed
           - - pip (Python package installer)
            
             - ### Setup
            
             - 1. Clone this repository:
               2. ```bash
                  git clone https://github.com/ovegkalgraff/automatic-qa.git
                  cd automatic-qa
                  ```

                  2. Install the required dependencies:
                  3. ```bash
                     pip install -r requirements.txt
                     ```

                     ### Running the Tests

                     To run the TV 2 Play Samsung app tests:

                     ```bash
                     # Run with pytest
                     pytest -v tests/test_tv2play_samsung.py

                     # To generate HTML reports
                     pytest -v tests/test_tv2play_samsung.py --html=report.html
                     ```

                     ### Test Results

                     Test results will be displayed in the console. Screenshots will be saved in the `screenshots` directory for debugging and documentation purposes.

                     - Successful tests will be marked with a green "PASSED"
                     - - Failed tests will be marked with a red "FAILED" and include error information
                       - - Test logs are saved to `tv2play_samsung_test.log`
                        
                         - ## License
                        
                         - This project is licensed under the MIT License - see the LICENSE file for details.
