from setuptools import setup, find_packages

setup(
    name="a3partitioner",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "biopython>=1.80",
    ],
    entry_points={
        'console_scripts': [
            'A3Partitioner=a3partitioner.cli:main',
        ],
    },
    author="Daan Jansen",
    author_email="jansendaan94@gmail.com",
    description="A bioinformatics tool for creating APOBEC3 and non-APOBEC3 partitions",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/DaanJansen94/a3partitioner",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.6",
)
