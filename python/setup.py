import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="advent-of-code-2018",
    version="0.1.0",
    author="Andrew Augustin",
    author_email="todo@todo.io",
    description="Fun coding with advent of code",
    license="MIT",
    keywords="advent-of-code python",
    url="https://github.com/AndreasAugustin/advent-of-code",
    packages=['src', 'test'],
    long_description=read('README.rst'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: AdventOfCode",
        "License :: MIT ",
    ],
)
