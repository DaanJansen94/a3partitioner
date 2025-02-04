from setuptools import setup, find_packages

setup(
    name="a3partitioner",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "biopython>=1.80,<=1.90",
    ],
    entry_points={
        'console_scripts': [
            'A3Partitioner=a3partitioner.cli:main',
        ],
    },
    python_requires='>=3.6,<4.0',
    include_package_data=True,
)