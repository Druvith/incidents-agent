import json
import time
from typing import Dict, Optional
import os
import sys


# where the mock data lives
DATA_PATH = "data/scenario_a"
def search_logs(level: str = "ERROR", limit: int = 5) -> list[Dict]:
    """
    Simulates searching the recent logs for a given keyword.
    
    Args:
    - keyword: The keyword to search for in the logs.
    - limit: The maximum number of log entries to return.
    Returns:
    - a list of log entries containing the keyword.
    """
    file_path = os.path.join(DATA_PATH, "logs.json")

    try:
        with open(file_path, "r") as f:
            logs = json.load(f)

        matches = []
        for log in logs:
            if log.get("level", "").upper() == level.upper():
                matches.append(log)
        
        return matches[-limit:] if limit > 0 else matches
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    

def get_recent_metrics(service_name: str, limit: int = 5) -> list[Dict]:
    """
    Fetches recent performance metrics for a specific service.
    
    The returned data contains:
    - latency_ms: Response time in milliseconds.
    - error_rate: Percentage of failed requests.
    - cpu_usage: Server CPU load (0-100).
    - timestamp: Time of recording.

    Args:
    - service_name: The name of the service (e.g., 'payment-service').
    - limit: The maximum number of entries to return (default 5).
    
    Returns:
    - A list of dictionary entries containing the metrics above.
    """

    file_path = os.path.join(DATA_PATH, "metrics.json")

    try:
        with open(file_path, "r") as f:
            metrics = json.load(f)

        matches = []
        for metric in metrics:
            if metric.get("service_name", "") == service_name:
                matches.append(metric)
        
        return matches[-limit:] if limit > 0 else matches
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def get_recent_commits(repository: Optional[str] = None, limit: int = 5) -> list[Dict]:
    """
    Fetches the deployment history (git commits) for a repository.
    
    The returned data contains:
    - message: The commit message.
    - author: Who made the change.
    - files_changed: List of files modified.
    - timestamp: When the code was deployed.

    Args:
    - repository: The repository name (usually matches the service name, e.g., 'payment-service').
    - limit: The maximum number of commits to return (default 5).
    
    Returns:
    - A list of commit objects.
    """

    file_path = os.path.join(DATA_PATH, "commits.json")

    try:
        with open(file_path, "r") as f:
            commits = json.load(f)

        matches = []
        for commit in commits:
            if commit.get("repository", "") == repository.lower():
                matches.append(commit)
        
        return matches[-limit:] if limit > 0 else matches
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []