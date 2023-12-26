@echo off

REM Check if virtual environment folder exists
IF NOT EXIST "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate the virtual environment
echo Activating virtual environment...
venv\Scripts\activate

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Start the application
echo Starting the application...
uvicorn app.main:app --reload
