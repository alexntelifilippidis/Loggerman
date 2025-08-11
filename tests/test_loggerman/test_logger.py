import logging

class TestLoggermanLogger:
    def test_debug_log(self, caplog, logger) -> None:
        caplog.set_level(logging.DEBUG)
        logger.debug("debug message")
        assert any("debug message" in record.message for record in caplog.records)
        assert any(record.levelno == logging.DEBUG for record in caplog.records)

    def test_info_log(self, caplog, logger) -> None:
        caplog.set_level(logging.INFO)
        logger.info("info message")
        assert any("info message" in record.message for record in caplog.records)
        assert any(record.levelno == logging.INFO for record in caplog.records)

    def test_warning_log(self, caplog, logger) -> None:
        caplog.set_level(logging.WARNING)
        logger.warning("warning message")
        assert any("warning message" in record.message for record in caplog.records)
        assert any(record.levelno == logging.WARNING for record in caplog.records)

    def test_error_log(self, caplog, logger) -> None:
        caplog.set_level(logging.ERROR)
        logger.error("error message")
        assert any("error message" in record.message for record in caplog.records)
        assert any(record.levelno == logging.ERROR for record in caplog.records)

    def test_critical_log(self, caplog, logger) -> None:
        caplog.set_level(logging.CRITICAL)
        logger.critical("critical message")
        assert any("critical message" in record.message for record in caplog.records)
        assert any(record.levelno == logging.CRITICAL for record in caplog.records)