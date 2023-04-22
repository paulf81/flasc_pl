"""The setup script."""

from pathlib import Path
from setuptools import setup, find_packages

# Package meta-data.
NAME = "flasc_pl"
DESCRIPTION = "FLASC [POLARS PORT] provides a rich suite of analysis tools for SCADA data filtering & analysis, wind farm model validation, field experiment design, and field experiment monitoring."
URL = "https://github.com/paulf81/flasc_pl"
EMAIL = "paul.fleming@nrel.gov"
AUTHOR = "NREL National Wind Technology Center"

# What packages are required for this module to be executed?
REQUIRED = [
    'floris>=3.1',
    'feather-format',
    'matplotlib>=3.6.3',
    'numpy',
    'openoa',
    'pandas>=1.5',
    'pyproj',
    'pytest',
    'SALib',
    'scipy',
    'sqlalchemy',
    'streamlit',
    'tkcalendar',
    'seaborn',
    'polars',
    'psycopg2-binary',
    'connectorx>=0.2.0a3'
]

ROOT = Path(__file__).parent
with open(ROOT / "flasc_pl" / "version.py") as version_file:
    VERSION = version_file.read().strip()

with open('README.rst') as readme_file:
    README = readme_file.read()

setup_requirements = [
    # Placeholder
]

test_requirements = [
    # Placeholder
]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=README,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(include=['flasc_pl']),
    entry_points={
        'console_scripts': [
            'flasc=flasc_pl.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=REQUIRED,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='flasc_pl',
    classifiers=[
        'Development Status :: Release',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
