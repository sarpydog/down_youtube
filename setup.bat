@echo off

:: Check if venv exists, if not, create it
if not exist venv (
    python3 -m venv venv
)

:: Activate virtual environment
call venv\Scripts\activate

:: Install dependencies
pip install pytube
pip install progressbar2