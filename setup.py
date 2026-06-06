from setuptools import setup, find_packages

setup(
    name="file-watcher-pro-backup-20260603_201616",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'file=file:main',
        ],
    },
)
