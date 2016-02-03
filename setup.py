from setuptools import setup
from release import assert_clean, get_version

assert_clean()

setup(
    name='release',
    version=get_version(),
    packages=['release'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
    ],
    entry_points={
        'console_scripts': [
            'release=release.main:main',
        ],
    },
)
