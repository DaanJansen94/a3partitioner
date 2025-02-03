#!/bin/bash

# Get the absolute path to the directory containing this script
INSTALL_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Create user's bin directory if it doesn't exist
mkdir -p "$HOME/.local/bin"

# Create symbolic link to A3Partitioner in user's bin
ln -sf "$INSTALL_DIR/A3Partitioner" "$HOME/.local/bin/A3Partitioner"

# Add ~/.local/bin to PATH if not already there
if ! grep -q "export PATH=\"\$HOME/.local/bin:\$PATH\"" "$HOME/.bashrc"; then
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$HOME/.bashrc"
    echo "Added ~/.local/bin to PATH in .bashrc"
fi

# Source .bashrc to apply changes immediately
source "$HOME/.bashrc"

echo "A3Partitioner has been installed and is ready to use!"
echo "Try running: A3Partitioner --help"
