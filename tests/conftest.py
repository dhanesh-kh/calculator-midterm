"""configure path for tests"""
import sys
import os

# Add the parent directory of the tests directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
