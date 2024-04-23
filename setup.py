"""Setup script for the projectpack package."""

from setuptools import setup

setup(
    name="projectpack",
    version="0.0.1",
    description="project package",
    maintainer="Mohammed Issa Abdul-Rahman",
    license="MIT",
    packages=["projectpack"],
    entry_points={"console_scripts": ["get_info=projectpack.main:get_info"]},
    long_description="""This package takes on an engineering or science topic
      as an argument and outputs the title,publication year,author names,institutions
      and countries those institutions are.""",
)
