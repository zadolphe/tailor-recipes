"""
test custom Django managment commands
"""

from unittest.mock import patch

from psycopg2 import OperationalError as Psychopg2Error

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


@patch('core.management.commands.wait_for_db.Command.check')
class CommandTests(SimpleTestCase):
    """Test commands"""

    def test_wait_for_db_ready(self, patched_check):
        """Test waiting for database if database ready"""
        patched_check.return_value = True

        call_command('wait_for_db')

        patched_check.assert_called_once_with(databases=['default'])

    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check):
        """test waiting for database when getting operational error"""
        """side effect here raises exception if db isnt running, raise 2 psychopg2
        errors and 3 operational errors. numbers are arbitrary"""
        patched_check.side_effect = [Psychopg2Error] * 2 + \
            [OperationalError] * 3 + [True]

        call_command('wait_for_db')

        """we raise 5 exceptions and then the last call is the return value so
        we are looking for 6 calls of the check method"""
        self.assertEqual(patched_check.call_count, 6)
        """here patched check is being called with the db set to default"""
        patched_check.assert_called_with(databases=['default'])

        """last we need to mock the sleep method"""
