# Minimal Python Project

A minimal, dependency-free Python project featuring a command-line interface that reads from and writes to a local `data.json` database.

## Project Structure
- `app.py`: The main interactive command-line application.
- `data.json`: Local JSON file acting as a flat-file database.
- `README.md`: Documentation for the project.
- `.gitignore`: Standard Git configuration file to exclude cache and IDE folders.

## Features
- **Zero Dependencies**: Uses only standard Python library packages (`json`, `os`, `sys`, `datetime`, `ctypes`).
- **Data Persistence**: Automatically reads from and writes back updates to the local `data.json`.
- **Colorful Terminal UI**: Includes cross-platform ANSI colors (configured to support Windows Command Prompt and PowerShell as well).

## Getting Started

### Prerequisites
- Python 3.6 or higher.

### Running the Application
Run the script using python:
```bash
python app.py
```
