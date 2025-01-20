"""
Ваша команда та ви розробляєте систему входу для веб-додатка,
і вам потрібно реалізувати тести на функцію для логування подій в системі входу.
Дано функцію, напишіть набір тестів для неї.
"""

import logging
import unittest
from unittest.mock import patch

def log_event(username: str, status: str):
    """
    Логує подію входу в систему.
    username: Ім'я користувача, яке входить в систему.
    status: Статус події входу:
    * success - успішний, логується на рівні інфо
    * expired - пароль застаріває і його слід замінити, логується на рівні warning
    * failed - пароль невірний, логується на рівні error
    """
    log_message = f"Login event - Username: {username}, Status: {status}"

    # Створення та налаштування логера
    logging.basicConfig(
        filename='login_system.log',
        level=logging.INFO,
        format='%(asctime)s - %(message)s'
        )
    logger = logging.getLogger("log_event")

    # Логування події
    if status == "success":
        logger.info(log_message)
    elif status == "expired":
        logger.warning(log_message)
    else:
        logger.error(log_message)

class TestLogEvent(unittest.TestCase):

    @patch('logging.getLogger')
    def test_log_success(self, mock_get_logger):
        # Налаштування mock-логера
        mock_logger = mock_get_logger.return_value

        # Виклик функції
        log_event("test_user", "success")

        # Перевірка, чи було викликано info із правильним повідомленням
        mock_logger.info.assert_called_once_with("Login event - Username: test_user, Status: success")

    @patch('logging.getLogger')
    def test_log_expired(self, mock_get_logger):
        # Налаштування mock-логера
        mock_logger = mock_get_logger.return_value

        # Виклик функції
        log_event("test_user", "expired")

        # Перевірка, чи було викликано warning із правильним повідомленням
        mock_logger.warning.assert_called_once_with("Login event - Username: test_user, Status: expired")

    @patch('logging.getLogger')
    def test_log_failed(self, mock_get_logger):
        # Налаштування mock-логера
        mock_logger = mock_get_logger.return_value

        # Виклик функції
        log_event("test_user", "failed")

        # Перевірка, чи було викликано error із правильним повідомленням
        mock_logger.error.assert_called_once_with("Login event - Username: test_user, Status: failed")

    @patch('logging.getLogger')
    def test_log_unknown_status(self, mock_get_logger):
        # Налаштування mock-логера
        mock_logger = mock_get_logger.return_value

        # Виклик функції із невідомим статусом
        log_event("test_user", "unknown")

        # Перевірка, чи було викликано error із правильним повідомленням
        mock_logger.error.assert_called_once_with("Login event - Username: test_user, Status: unknown")

if __name__ == "__main__":
    unittest.main()
