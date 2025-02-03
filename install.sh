#!/bin/bash

# Get the absolute path to the directory containing this script
INSTALL_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Add the repository directory to PATH if not already there
if ! grep -q "export PATH=\"$INSTALL_DIR:\$PATH\"" ~/.bashrc; then
    echo "export PATH=\"$INSTALL_DIR:\$PATH\"" >> ~/.bashrc
    echo "Added A3Partitioner directory to PATH"
fi

# Source .bashrc to apply changes immediately
source ~/.bashrc

echo "A3Partitioner has been installed and is ready to use!"
echo "Try running: A3Partitioner --help"
