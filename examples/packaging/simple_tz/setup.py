"""
setup.py - Set up script for sample project
"""

# TODO: import setup and find_packages from the setuptools module
...

import setuptools


# TODO: note the call to the setup() function
setup(
    ...,  # TODO: set the package name to 'simple_tz'
    ...,   # TODO: set `version` to '1.0.0'
    ...,  # TODO: set `description` to a string
    ...,  # TODO: set `platforms` to a list with one string element 'all'
    ...,  # TODO: set `install_requires` to a list with one string element 'pytz'
    ...,  # TODO: set `author` to a string with your name
    ...,  # TODO: set `author_email` to a string
    # TODO: review the remaining keyword arguments
    # (no code change required)
    long_description='Typically the README description is put here',
    url='http://www.pythonchamp.com/simple_tz',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    license='MIT',
    keywords='simple_tz timezone datetime',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
    ],
)
