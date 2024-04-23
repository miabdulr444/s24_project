"""A package for retrieving information from the OpenAlex API."""

import projectpack


def test_hello():
    """Welcome message."""
    assert projectpack.hello("Guys") == "Hi there Guys"


def get_info(kinetics):
    """Test the get_info function in the projectpack module."""
    assert projectpack.get_info("kinetics") == 200
