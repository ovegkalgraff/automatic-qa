import os
import sys

def check_file_exists(filepath, description):
    if os.path.isfile(filepath):
        print(f"✅ {description} found: {filepath}")
        return True
    else:
        print(f"❌ {description} NOT found: {filepath}")
        return False

def check_directory_exists(dirpath, description):
    if os.path.isdir(dirpath):
        print(f"✅ {description} found: {dirpath}")
        return True
    else:
        print(f"❌ {description} NOT found: {dirpath}")
        return False

def main():
    print("Checking Automatic QA Project Structure...")
    print("-" * 50)
    
    # Check root level files
    root_dir = os.path.dirname(os.path.abspath(__file__))
    readme = os.path.join(root_dir, "README.md")
    requirements = os.path.join(root_dir, "requirements.txt")
    pytest_ini = os.path.join(root_dir, "pytest.ini")
    
    # Check directories
    tests_dir = os.path.join(root_dir, "tests")
    
    # Check test files
    philips_test = os.path.join(tests_dir, "test_philips.py")
    samsung_test = os.path.join(tests_dir, "test_samsung.py")
    lg_test = os.path.join(tests_dir, "test_lg.py")
    conftest = os.path.join(tests_dir, "conftest.py")
    
    # Perform checks
    files_ok = (
        check_file_exists(readme, "README.md") and
        check_file_exists(requirements, "requirements.txt") and
        check_file_exists(pytest_ini, "pytest.ini")
    )
    
    dirs_ok = check_directory_exists(tests_dir, "tests directory")
    
    test_files_ok = (
        check_file_exists(philips_test, "Philips test file") and
        check_file_exists(samsung_test, "Samsung test file") and
        check_file_exists(lg_test, "LG test file") and
        check_file_exists(conftest, "conftest.py file")
    )
    
    print("-" * 50)
    if files_ok and dirs_ok and test_files_ok:
        print("✅ Project structure is correct!")
        print("\nTo run the tests, use the following commands:")
        print("1. Install dependencies:")
        print("   pip install -r requirements.txt")
        print("\n2. Run tests:")
        print("   pytest")
        print("\nOr run specific test files:")
        print("   pytest tests/test_philips.py")
        print("   pytest tests/test_samsung.py")
        print("   pytest tests/test_lg.py")
        return 0
    else:
        print("❌ Project structure has issues!")
        return 1

if __name__ == "__main__":
    sys.exit(main()) 