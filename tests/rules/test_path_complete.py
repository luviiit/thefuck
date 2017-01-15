import pytest
from thefuck.rules.path_complete import match, get_new_command
from tests.utils import Command


@pytest.mark.parametrize('command', [
    Command(script='cd baz', stderr='cd: baz: No such file or directory')])
def test_match(command):
    assert match(command)


@pytest.mark.parametrize('command', [
    Command(script='cd baz', stderr=''), Command()])
def test_not_match(command):
    assert not match(command)


@pytest.mark.parametrize('command', [
    (Command('cd baz'))])
def test_get_new_command(command):
    # Test if completed file paths exist
