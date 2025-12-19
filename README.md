# colorLite

**colorLite** is a lightweight Python logging utility that provides colorful console output for different log levels.

## Features

- **Colorful Output**: Each log level is displayed with a unique color for better readability.
- **Lightweight**: No external dependencies required.
  
## Installation
`pip install colorlite`
## Usage

```python
from colorLite import Logger

# Create a Logger instance
logger = Logger()

# Log messages with various levels
logger.debug("This is a debug message.")
logger.info("This is an info message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.critical("This is a critical message.")
