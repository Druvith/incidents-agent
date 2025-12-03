# test_data.py
import sys
import os

# Add the parent directory (project root) to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from tools import get_recent_metrics, search_logs, get_recent_commits

print("--- Metrics ---")
print(get_recent_metrics("payment-service"))

print("\n--- Logs (Errors) ---")
print(search_logs("ERROR"))

print("\n--- Commits ---")
print(get_recent_commits("payment-service"))