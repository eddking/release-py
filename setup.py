from setuptools import setup
from release import get_version, assert_unmodified, get_released_version

assert_unmodified()

setup(
    name='release-py',
    version=get_version(),
    packages=['release'],
    description='a utility for enforcing release process and automating build versioning with git',
    author='Edmund King',
    author_email='edmundking2002@yahoo.co.uk',
    license = "MIT",
    url = 'https://github.com/eddking/release-py',
    download_url = 'https://github.com/eddking/release-py/tarball/' + get_released_version(),
    install_requires=['docopt'],
    keywords = ['release', 'git', 'versioning'],
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
