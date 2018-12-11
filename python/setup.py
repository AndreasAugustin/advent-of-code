import os
from os.path import basename
from os.path import splitext
from glob import glob
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


#datadir = os.path.join('..', 'data')
#datafiles = [(d, [os.path.join(d, f) for f in files])
#             for d, folders, files in os.walk(datadir)]

setup(
    name="advent-of-code-2018",
    version="0.1.0",
    author="Andrew Augustin",
    author_email="todo@todo.io",
    description="Fun coding with advent of code",
    long_description=read('README.rst'),
    keywords="advent-of-code python",
    license="MIT",
    url="https://github.com/AndreasAugustin/advent-of-code",
    packages=find_packages('aoc'),
    package_dir={'': 'aoc'},
    py_modules=[splitext(basename(path))[0] for path in glob('aoc/*.py')],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: AdventOfCode",
        "License :: MIT ",
    ],
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
    entry_points={
          'console_scripts': [
              'aoc = __init__:main'
          ]
    },
    install_requires=['argparse', 'attr', 'importlib'],
    project_urls={
        'Advent of code': 'https://adventofcode.com/',
        'Source': 'https://github.com/AndreasAugustin/advent-of-code"',
    },
    #data_files=datafiles,
    #include_package_data=True,
    #package_data={'data': ['../data/*']},
)
