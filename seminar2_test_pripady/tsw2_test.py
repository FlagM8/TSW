import pytest
from .tsw2 import is_valid_password

@pytest.mark.parametrize(
    "password,expected",
    [
        ("Abcdefg1", True),    
        ("Abc1", False),   
        ("Abcdefgh", False), 
        ("abcdefg1", False),  
        ("ABCDEFG1", False),
        ("12345678", False),   
    ]
)
def test_is_valid_password(password, expected):
    assert is_valid_password(password) == expected


#on by pytest --maxfail=1 --disable-warnings -v --html=report.html