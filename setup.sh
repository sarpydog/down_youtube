#!/bin/bash

# Check if venv exists, if not, create it
if [ ! -d "venv" ]; then
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install pytube
pip install progressbar2
