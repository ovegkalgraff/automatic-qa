#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Test runner script for TV 2 Play Smart TV app testing.
"""

import os
import sys
import glob
import argparse
import subprocess
from datetime import datetime

def create_directories():
    """Create necessary directories if they don't exist."""
    os.makedirs("artifacts/screenshots", exist_ok=True)
    os.makedirs("artifacts/reports", exist_ok=True)

def run_tests(platforms, parallel=False, html_report=True, verbose=True):
    """Run tests for specified platforms."""
    create_directories()
    
    # Build command
    cmd = ["python", "-m", "pytest"]
    
    # Add test files based on platforms
    if "all" in platforms:
        cmd.append("tests/")
    else:
        for platform in platforms:
            # Include all test files that contain the platform name
            platform_files = glob.glob(f"tests/test_*{platform}*.py")
            cmd.extend(platform_files)
    
    # Add options
    if verbose:
        cmd.append("-v")
    
    if parallel:
        cmd.append(f"-n {2 if len(platforms) > 1 else 1}")
    
    if html_report:
        timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
        report_path = f"artifacts/reports/report_{'-'.join(platforms)}_{timestamp}.html"
        cmd.append(f"--html={report_path}")
    
    # Run the command
    print(f"Running command: {' '.join(cmd)}")
    result = subprocess.run(cmd)
    
    return result.returncode

def main():
    parser = argparse.ArgumentParser(description="Run TV 2 Play Smart TV app tests")
    parser.add_argument("--platforms", "-p", nargs="+", default=["all"],
                        choices=["all", "samsung", "lg", "philips"],
                        help="Platforms to test (default: all)")
    parser.add_argument("--parallel", action="store_true",
                        help="Run tests in parallel")
    parser.add_argument("--no-html", action="store_true",
                        help="Disable HTML report generation")
    parser.add_argument("--quiet", "-q", action="store_true",
                        help="Run tests without verbose output")
    
    args = parser.parse_args()
    
    print(f"Running tests for platforms: {', '.join(args.platforms)}")
    return run_tests(
        platforms=args.platforms,
        parallel=args.parallel,
        html_report=not args.no_html,
        verbose=not args.quiet
    )

if __name__ == "__main__":
    sys.exit(main()) 