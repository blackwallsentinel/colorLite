class Logger:
    def debug(self, message):
        print(f"\033[94m\033[1mDEBUG:\033[0m {message}")

    def info(self, message):
        print(f"\033[92m\033[1mINFO:\033[0m {message}")

    def warning(self, message):
        print(f"\033[93m\033[1mWARNING:\033[0m {message}")

    def error(self, message):
        print(f"\033[91m\033[1mERROR:\033[0m {message}")

    def critical(self, message):
        print(f"\033[95m\033[1mCRITICAL:\033[0m {message}")

# Example usage
logger = Logger()
logger.debug("This is a debug message.")
logger.info("This is an info message.")
logger.warning("This is a warning message.")
logger.error("This is an error message.")
logger.critical("This is a critical message.")

