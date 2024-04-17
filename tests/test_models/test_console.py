#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from console import parse_value, HBNBCommand
from unittest.mock import patch
from io import StringIO
from models import storage


class test_Console(test_basemodel):
    """Class to test console"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.parse_tests = [
            "123",
            "123.4",
            '"a_b_c"',
            '"a\\"s"',
            '"\\"\'"',
            '"\\"',
            "lol",
        ]
        self.parse_res = [123, 123.4, "a b c", 'a"s', "\"'", None, None]

    def test_parse_value(self):
        """tests the parse_value function"""
        for t, res in zip(self.parse_tests, self.parse_res):
            self.assertEqual(parse_value(t), res)

    @patch("sys.stdout", new_callable=StringIO)
    def test_create(self, mock_stdout):
        """test the create command"""
        cmd = HBNBCommand()

        before = len(storage.all())
        cmd.onecmd('create State name="Florida"')

        self.assertEqual(len(storage.all()), before + 1)
        self.assertEqual(
            storage.all()[f"State.{mock_stdout.getvalue()[:-1]}"].name,
            "Florida"
        )
        state_id = mock_stdout.getvalue()

        mock_stdout.seek(0)
        mock_stdout.truncate()

        cmd.onecmd('create City name="California" state_id="{state_id}"')
