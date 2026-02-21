from unittest.mock import patch
from app.exercise import *

def test_logger_prints_correct_message():
    logger = Logger()

    with patch("builtins.print") as mock_print:
        logger.log("hello")

        mock_print.assert_called_once_with("[LOG]: hello")

def test_send():
    service = NotificationService()

    with patch("builtins.print") as mock_print:
        service.send("recipient", "message")

        mock_print.assert_called_once_with("[NOTIFY recipient]: message")

