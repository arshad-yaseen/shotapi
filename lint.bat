@echo off
SETLOCAL

REM Stop on first error
set -e

REM Directory containing the script file
SET dir=%~dp0

echo Formatting code with Black...
black %dir%

echo Running Flake8...
flake8 %dir%

echo Running Bandit for security checks...
bandit -c pyproject.toml -r %dir%

echo Linting and formatting completed successfully!

ENDLOCAL
