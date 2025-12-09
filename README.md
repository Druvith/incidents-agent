# Incident Response Team using Google's ADK

## Overview

This project demonstrates how to build a multi-agent system for automated incident response using Google's Agent Development Kit (ADK). It simulates a team of agents that work together to diagnose the root cause of a technical incident by analyzing logs, metrics, and recent code changes.

## Capabilities

- **Parallel Data Collection**: A `ParallelAgents` orchestrator fans out requests to specialized agents that investigate different data sources simultaneously:
  - **Log Investigator**: Searches for error logs.
  - **Metrics Investigator**: Fetches recent performance metrics.
  - **Commits Investigator**: Looks up recent code deployments.
- **Sequential Analysis**: A `SequentialAgent` receives the collected data, correlates the findings, and generates a root-cause analysis report with a confidence score.
- **Dynamic Scenarios**: The data path is configurable via an environment variable, allowing you to easily switch between different incident scenarios without changing the code.


## Getting Started

### Prerequisites

- Python 3.9+
- uv (for fast dependency management)

### Installation & Running

1.  **Clone the repository:**
    ```sh
    git clone <your-repository-url>
    cd <repository-name>
    ```

2.  **Create a virtual environment and install dependencies:**
    This project uses `uv` for performance.
    ```sh
    # Create a virtual environment
    python -m venv .venv
    source .venv/bin/activate

    # Install dependencies using uv
    uv pip install -r requirements.txt
    ```

3.  **Run the agent:**
    You can run the agent directly from the command line:
    ```sh
    adk run incidents_agent
    ```
    Or, you can use the web interface for a more visual and debug-friendly experience:
    ```sh
    adk web --port 8000
    ```

## Extending the Tools

You can easily add new tools or modify existing ones to connect to real data sources (e.g., Splunk, Datadog, GitHub API). The tools are simple Python functions located in `incidents_agent/tools.py`.

For more information on building agents and tools with the ADK, please refer to the official ADK documentation.

## Acknowledgments

This project is built with the help of these amazing technologies:
- Google's Agent Development Kit (ADK)
- Gemini
