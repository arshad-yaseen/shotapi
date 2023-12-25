#!/bin/bash

# Stop on first error
set -e

# Directory containing the script file
dir="$(dirname "$0")"

echo "Formatting code with Black..."
black $dir

echo "Running Flake8..."
flake8 $dir

echo "Running Bandit for security checks..."
bandit -r $dir

echo "Linting and formatting completed successfully!"
