"""Setup file for projectpack."""

from setuptools import setup

setup(
    name="projectpack",
    version="0.0.1",
    description="project package",
    maintainer="Mohammed Issa Abdul-Rahman",
    license="MIT",
    packages=["projectpack"],
    entry_points={"console_scripts": ["get_info=projectpack.main:get_info"]},
    long_description="""This is a query tool for the OpenAlex database.""",
)
