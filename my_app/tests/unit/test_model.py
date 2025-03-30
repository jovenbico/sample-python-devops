import pytest
from domain import ModelError, User

def test_user_initialization():
    user = User(id=1, name="Alice")
    assert user.name == "Alice"