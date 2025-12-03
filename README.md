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

2.  **Install uv (if you haven't already):**

    You can install `uv` using the recommended `curl` method:
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```
    Alternatively, if you have `pip` installed, you can use:
    ```bash
    pip install uv
    ```

3.  **Install dependencies with uv:**
    ```bash
    uv sync
    ```
    This will create a virtual environment in `.venv` and install `httpx` and `mcp[cli]` as defined in `pyproject.toml`.

## Gemini CLI Setup

To interact with this tool, you'll need the Gemini CLI. If you don't have it installed, follow these steps:

### Install the Gemini CLI

```bash
uv pip install --upgrade gemini-cli
```

### Obtain an API Key

To use the Gemini models, you need an API key. You can obtain one from:

*   **Google AI Studio**: Visit [https://aistudio.google.com/](https://aistudio.google.com/) to generate an API key for free.
*   **Google Cloud**: If you're a Google Cloud user, you can manage API keys through the Google Cloud Console.

Once you have your API key, you should set it as an environment variable named `GEMINI_API_KEY`:

```bash
export GEMINI_API_KEY="your-api-key-here"
```

### Introduction to Gemini CLI

The Gemini CLI allows you to chat with Gemini models and interact with tools like the ones provided in this repository. To start a chat session, simply run:

```bash
gemini chat
```

When the CLI starts, it will provide context about your project (like the file structure). You can then type your prompts, and the Gemini model will respond, potentially using the tools defined in `weather.py`.

## Usage

This tool is designed to be used with a Gemini-powered CLI. Once the environment is set up and the `mcp` server is running, you can interact with the `get_alerts` and `get_forecast` tools.

### Running the MCP Server

To start the `mcp` server, run the `weather.py` file:
```bash
uv run weather.py
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
- `weather.py`: Main entry point for the MCP server. Contains the core logic for interacting with the NWS API.
- `main.py`: Basic entry point example.
- `test_weather.py`: Basic tests for the application.
- `pyproject.toml`: Project metadata and dependencies.
- `README.md`: This file.

## Testing

To run the tests, you will need to have `pytest` installed. You can run the tests using `uv`:

```bash
uv run pytest test_weather.py
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For any questions or issues, please contact qhoang@wm.edu.
