@echo off
REM This script sets up the Python project environment on Windows.

echo "Project Setup Script for Windows"

REM Check if python is installed and available in PATH
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo "Error: Python is not installed or not added to your PATH."
    echo "Please install Python from python.org and ensure it's in your system's PATH."
    pause
    exit /b 1
)

REM Create virtual environment
echo "Creating virtual environment named 'myenv'"
python -m venv myenv

REM Activate virtual environment
echo "Activating virtual environment"
call myenv\Scripts\activate.bat

REM Install packages from requirements.txt
echo "Installing project requirements"
pip install -r requirements.txt

echo.
echo All set! The virtual environment 'myenv' is ready and dependencies are installed.
echo To activate it in the future, run: myenv\Scripts\activate.bat

REM Keep the command prompt open to see the output.
pause
