# Weather CLI Tool

## Project Description
This project provides a command-line interface (CLI) tool for fetching weather forecasts and active weather alerts using the National Weather Service (NWS) API. It leverages `mcp[cli]` for tool exposure, allowing integration with Gemini-powered assistants.

## Features
- Get current weather alerts for any US state.
- Get a detailed weather forecast for a specific latitude and longitude.

## Requirements
- Python 3.11 or higher

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/weather.git
    cd weather
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -e .
    ```
    This will install `httpx` and `mcp[cli]` as defined in `pyproject.toml`.

## Usage

This tool is designed to be used with a Gemini-powered CLI. Once the environment is set up and the `mcp` server is running, you can interact with the `get_alerts` and `get_forecast` tools.

### Running the MCP Server

To start the `mcp` server, run the `main.py` file:
```bash
python main.py
```
This will start the server, making the `get_alerts` and `get_forecast` tools available.

### Example: Getting Weather Forecast

You can ask your Gemini CLI for the weather in a specific location. The CLI will use web search to find the latitude and longitude and then call `get_forecast`.

```
What's the weather in Williamsburg, VA?
```

### Example: Getting Weather Alerts

You can ask your Gemini CLI for active weather alerts in a specific state. The CLI will call `get_alerts`.

```
What are the active weather alerts in Virginia?
```

## Project Structure
- `main.py`: Entry point for the MCP server.
- `weather.py`: Contains the core logic for interacting with the NWS API and defines `get_alerts` and `get_forecast` tools.
- `pyproject.toml`: Project metadata and dependencies.
- `README.md`: This file.

## Contact
For any questions or issues, please contact qhoang@wm.edu.
