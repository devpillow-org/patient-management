#!/bin/bash

VIRTUALENV="$(pwd -P)/.venv"
EXAMPLE_ENVFILE="$(pwd -P)/example.env"
PYTHON="${PYTHON:-python3}"

# Validate the minimum required Python version
COMMAND="${PYTHON} -c 'import sys; exit(1 if sys.version_info < (3, 12) else 0)'"
PYTHON_VERSION=$(eval "${PYTHON} -V")

eval $COMMAND || {
  echo "---------------------------------------------------------------------------------"
  echo "ERROR: Unsupported Python version: ${PYTHON_VERSION}. Patient Management requires"
  echo "Python 3.12 or later. To specify an alternate Python executable, set the PYTHON"
  echo "environment variable. For example:"
  echo ""
  echo "  sudo PYTHON=/usr/bin/python3.12 ./configure.sh"
  echo ""
  echo "To show your current Python version: ${PYTHON} -V"
  echo "---------------------------------------------------------------------------------"
  exit 1
}
echo "Using ${PYTHON_VERSION}"

# Remove the existing virtual environment (if any)
if [ -d "$VIRTUALENV" ]; then
  COMMAND="rm -rf \"${VIRTUALENV}\""
  echo "Removing old virtual environment ..."
  eval $COMMAND
else
  echo "No virtual environment to remove. Continuing ..."
  WARN_MISSING_VENV=1
fi


# Create a new virtual environment
COMMAND="${PYTHON} -m venv \"${VIRTUALENV}\""
echo "Creating a new virtual environment at ${VIRTUALENV} ..."
eval $COMMAND || {
  echo "--------------------------------------------------------------------"
  echo "ERROR: Failed to create the virtual environment. Check that you have"
  echo "the required system packages installed and the following path is"
  echo "writable: ${VIRTUALENV}"
  echo "--------------------------------------------------------------------"
  exit 1
}

# Activate the virtual environment
source "${VIRTUALENV}/bin/activate"

# Upgrade pip
COMMAND="pip install --upgrade pip"
echo "Updating pip ($COMMAND)..."
eval $COMMAND || exit 1
pip -V

# Install required Python packages
COMMAND="pip install -r requirements-dev.txt"
echo "Installing development dependencies ($COMMAND)..."
eval $COMMAND || exit 1

COMMAND="pip install -r requirements.txt"
echo "Installing application dependencies ($COMMAND)..."
eval $COMMAND || exit 1

# Installation of pre-commit
COMMAND="pre-commit install"
echo "Installing pre-commit hooks..."
eval $COMMAND || exit 1

# Set environment file
COMMAND="cp $EXAMPLE_ENVFILE $(pwd -P)/.env"
if [ ! -s "$(pwd -P)/.env" ]; then
  echo "Creating .env file ..."
  eval $COMMAND || exit 1
elif [ -f "$(pwd -P)/.env" ]; then
  echo "Copping required variables (.env file are empty)"
else
  echo "Skipping set environment variables (.env file are populated)"
fi

echo "--------------------------------------------------------------------"
echo "Confiruation complete! You can start your development after set the"
echo "environment variables at:"
echo "  ./.env"
echo "Don't forget to apply the migrations:"
echo "  > make migrate"
echo "--------------------------------------------------------------------"
