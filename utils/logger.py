import logging
import json
import sys

class StructuredLogger:
    def __init__(self, name="shadowmergeplus", level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(self.json_formatter())
        self.logger.handlers = [handler]

    def json_formatter(self):
        class JsonLogFormatter(logging.Formatter):
            def format(self, record):
                log_record = {
                    "level": record.levelname,
                    "logger": record.name,
                    "message": record.getMessage(),
                    "time": self.formatTime(record, self.datefmt),
                }
                if record.exc_info:
                    log_record["exception"] = self.formatException(record.exc_info)
                return json.dumps(log_record)
        return JsonLogFormatter()

    def info(self, message, **fields):
        self.logger.info(self._format_msg(message, fields))

    def warning(self, message, **fields):
        self.logger.warning(self._format_msg(message, fields))

    def error(self, message, **fields):
        self.logger.error(self._format_msg(message, fields))

    def debug(self, message, **fields):
        self.logger.debug(self._format_msg(message, fields))

    def _format_msg(self, message, fields):
        if fields:
            return f"{message} | {json.dumps(fields)}"
        return message
