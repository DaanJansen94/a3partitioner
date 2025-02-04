#!/bin/bash

# Get the absolute path to the directory containing this script
INSTALL_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Add the repository directory to PATH if not already there
if ! grep -q "export PATH=\"$INSTALL_DIR:\$PATH\"" ~/.bashrc; then
    echo "export PATH=\"$INSTALL_DIR:\$PATH\"" >> ~/.bashrc
    echo "Added A3Partitioner directory to PATH"
fi

echo "A3Partitioner has been installed!"
echo "Please run this command to complete installation:"
echo "source ~/.bashrc"
echo ""
echo "Then you can use 'A3Partitioner --help' from anywhere"
