import logging
import sys

from colorama import Fore, Style, init

from src.loggerman.singleton import SingletonMeta

init(autoreset=True)


class LoggermanLogger(metaclass=SingletonMeta): # type: ignore[misc]
    """
    A singleton logger class that outputs colorized and emoji-enhanced log messages to stdout.

    :param name: Logger name, defaults to "Loggerman"
    :type name: str, optional
    :param level: Logging level as a string (e.g., "INFO", "DEBUG"), defaults to "INFO"
    :type level: str, optional
    :param propagate: Whether the logger should propagate messages to ancestor loggers, defaults to False
    :type propagate: bool, optional
    """

    COLORS = {
        logging.DEBUG: Fore.CYAN,
        logging.INFO: Fore.GREEN,
        logging.WARNING: Fore.YELLOW,
        logging.ERROR: Fore.RED,
        logging.CRITICAL: Fore.RED + Style.BRIGHT,
    }

    EMOJIS = {
        logging.DEBUG: "🐞",
        logging.INFO: "✨",
        logging.WARNING: "⚠️",
        logging.ERROR: "❌",
        logging.CRITICAL: "💥",
    }

    def __init__(self, name: str = "Loggerman", level: str = "INFO", propagate: bool = False) -> None:
        """
        Initialize the LoggermanLogger instance.

        :param name: Logger name, defaults to "Loggerman"
        :type name: str, optional
        :param level: Log level string, e.g. "INFO", "DEBUG", defaults to "INFO"
        :type level: str, optional
        :param propagate: Whether to propagate logs to parent loggers, defaults to False
        :type propagate: bool, optional
        :return: None
        :rtype: None
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level.upper())

        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(level.upper())
        handler.setFormatter(self._ColoredFormatter())

        self.logger.handlers.clear()
        self.logger.addHandler(handler)
        self.logger.propagate = propagate

    class _ColoredFormatter(logging.Formatter):
        """
        Custom formatter to add colors and emojis to log messages.

        :return: None
        :rtype: None
        """

        def format(self, record: logging.LogRecord) -> str:
            """
            Format the log record with color and emoji.

            :param record: The log record to format
            :type record: logging.LogRecord
            :return: The formatted log message string with colors and emojis
            :rtype: str
            """
            color = LoggermanLogger.COLORS.get(record.levelno, "")
            emoji = LoggermanLogger.EMOJIS.get(record.levelno, "")
            time = self.formatTime(record, "%Y-%m-%d %H:%M:%S")
            message = super().format(record)
            return f"{color}{emoji} [{time}] [{record.name}] {record.levelname}: {message}{Style.RESET_ALL}"

    def debug(self, msg: str) -> None:
        """
        Log a debug-level message.

        :param msg: The message to log
        :type msg: str
        :return: None
        :rtype: None
        """
        self.logger.debug(msg)

    def info(self, msg: str) -> None:
        """
        Log an info-level message.

        :param msg: The message to log
        :type msg: str
        :return: None
        :rtype: None
        """
        self.logger.info(msg)

    def warning(self, msg: str) -> None:
        """
        Log a warning-level message.

        :param msg: The message to log
        :type msg: str
        :return: None
        :rtype: None
        """
        self.logger.warning(msg)

    def error(self, msg: str) -> None:
        """
        Log an error-level message.

        :param msg: The message to log
        :type msg: str
        :return: None
        :rtype: None
        """
        self.logger.error(msg)

    def critical(self, msg: str) -> None:
        """
        Log a critical-level message.

        :param msg: The message to log
        :type msg: str
        :return: None
        :rtype: None
        """
        self.logger.critical(msg)