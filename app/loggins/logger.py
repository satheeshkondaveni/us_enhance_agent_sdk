from loguru import logger

# Configure global logger
logger.add("logs/agent.log", rotation="1 MB", level="INFO")

def get_logger():
    return logger
