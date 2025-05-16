# Automatic QA

Repository for automated quality assurance tools and scripts.

## TV 2 Play App Regression Tests

This repository contains automated regression tests for TV 2 Play applications on different platforms:

### Samsung App Tests

The TV 2 Play Samsung app tests verify that:
1. The page loads correctly
2. 2. UI elements are present and functional
   3. 3. The application responds appropriately to different screen resolutions
     
      4. ### LG App Tests
     
      5. The TV 2 Play LG app tests verify that:
      6. 1. The page loads correctly
         2. 2. UI elements are present and functional
            3. 3. The application responds appropriately to different screen resolutions
               4. 4. Navigation using remote control simulation works properly
                  5. 5. Performance metrics meet quality standards
                    
                     6. ### Philips App Tests
                    
                     7. The TV 2 Play Philips app tests verify that:
                     8. 1. The page loads correctly
                        2. 2. UI elements are present and functional
                           3. 3. The application responds appropriately to different screen resolutions
                              4. 4. Navigation using remote control simulation works properly
                                 5. 5. Performance metrics meet quality standards
                                    6. 6. Philips-specific features and interactions are working correctly
                                      
                                       7. ## Prerequisites
                                      
                                       8. - Python 3.8 or higher
                                          - - Chrome browser installed
                                            - - pip (Python package installer)
                                             
                                              - ## Setup
                                             
                                              - 1. Clone this repository:
                                                2. ```bash
                                                   git clone https://github.com/ovegkalgraff/automatic-qa.git
                                                   cd automatic-qa
                                                   ```

                                                   2. Install the required dependencies:
                                                   3. ```bash
                                                      pip install -r requirements.txt
                                                      ```

                                                      ## Running the Tests

                                                      ### Samsung App Tests

                                                      ```bash
                                                      # Run with pytest
                                                      pytest -v tests/test_tv2play_samsung.py

                                                      # To generate HTML reports
                                                      pytest -v tests/test_tv2play_samsung.py --html=samsung_report.html
                                                      ```

                                                      ### LG App Tests

                                                      ```bash
                                                      # Run with pytest
                                                      pytest -v tests/test_tv2play_lg.py

                                                      # To generate HTML reports
                                                      pytest -v tests/test_tv2play_lg.py --html=lg_report.html
                                                      ```

                                                      ### Philips App Tests

                                                      ```bash
                                                      # Run with pytest
                                                      pytest -v tests/test_tv2play_philips.py

                                                      # To generate HTML reports
                                                      pytest -v tests/test_tv2play_philips.py --html=philips_report.html
                                                      ```

                                                      ## Test Results

                                                      Test results will be displayed in the console. Screenshots will be saved in the `screenshots` directory for debugging and documentation purposes.

                                                      1. Successful tests will be marked with a green "PASSED"
                                                      2. 2. Failed tests will be marked with a red "FAILED" and include error information
                                                         3. 3. Test logs are saved to `tv2play_samsung_test.log`, `tv2play_lg_test.log`, and `tv2play_philips_test.log`
                                                           
                                                            4. ## License
                                                           
                                                            5. This project is licensed under the MIT License - see the LICENSE file for details.
