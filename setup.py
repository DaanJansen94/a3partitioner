from setuptools import setup, find_packages
import os
import site
import sys

def _post_install(dir):
    # Add bin to PATH during installation
    path_file = os.path.join(dir, 'a3partitioner.pth')
    with open(path_file, 'w') as f:
        f.write(os.path.join(os.getcwd(), 'bin'))

setup(
    name="a3partitioner",
    version="0.1.0",
    packages=find_packages(),
    scripts=['bin/A3Partitioner'],
    install_requires=[
        "biopython>=1.80",
    ],
    data_files=[
        ('bin', ['bin/A3Partitioner']),
    ],
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

if 'install' in sys.argv:
    _post_install(site.getsitepackages()[0])