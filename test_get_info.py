"""Module containing unit tests for the projectpack module."""

import projectpack


def test_hello():
    """
    Test the hello function in projectpack.

    Checks if the hello function returns the expected greeting.

    Returns
    -------
        None

    """
    assert projectpack.hello("Guys") == "Hi there Guys"


def get_info(kinetics):
    """
    Test the get_info function in projectpack.

    Args
    ----
    kinetics: Some parameter representing kinetics.

    Returns
    -------
        None.

    """
    assert projectpack.get_info("kinetics") == 200
