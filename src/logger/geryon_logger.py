import configparser
import logging


def __get_logging_level(level: str) -> int:
    level_uppercase = level.upper()
    if level_uppercase == "CRITICAL" or level_uppercase == "FATAL":
        return logging.CRITICAL
    if level_uppercase == "ERROR":
        return logging.ERROR
    if level_uppercase == "WARNING" or level_uppercase == "WARN":
        return logging.WARNING
    if level_uppercase == "INFO":
        return logging.INFO
    if level_uppercase == "DEBUG":
        return logging.DEBUG
    raise ValueError(f"Invalid logger level: {level}")


def build_logger(config: configparser.ConfigParser) -> logging.Logger:
    logger_name = config.get("logger", "name", fallback="geryon-fuse")
    logging_level = __get_logging_level(config.get("logger", "level", fallback="DEBUG"))
    logging_format = config.get("logger", "format", fallback="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    logger = logging.getLogger(name=logger_name)
    logger.setLevel(level=logging_level)
    logger_console_handler = logging.StreamHandler()
    logger_console_handler.setLevel(logging_level)
    logger_formatter = logging.Formatter(logging_format)
    logger_console_handler.setFormatter(logger_formatter)
    logger.addHandler(logger_console_handler)

    return logger
