@echo off
REM AI Virtual Career Counsellor - Initial Setup Script (Windows)
REM This script handles the initial setup and installation

REM Change to the project root directory (parent of scripts folder)
cd /d "%~dp0\.."

echo 🎯 AI Virtual Career Counsellor - Initial Setup
echo ===============================================

REM Check Python version
echo 🐍 Checking Python version...
python --version >nul 2>&1
if %errorlevel% equ 0 (
    for /f "tokens=*" %%i in ('python --version') do echo ✅ Found: %%i
) else (
    echo ❌ Python is not installed or not in PATH
    echo Please install Python 3.9+ from https://python.org
    pause
    exit /b 1
)

REM Create virtual environment
echo 🏗️  Creating virtual environment...
if not exist "venv" (
    python -m venv venv
    if %errorlevel% equ 0 (
        echo ✅ Virtual environment created: venv\
    ) else (
        echo ❌ Failed to create virtual environment
        pause
        exit /b 1
    )
) else (
    echo ✅ Virtual environment already exists: venv\
)

REM Activate virtual environment
echo 🔄 Activating virtual environment...
call venv\Scripts\activate.bat

if %errorlevel% equ 0 (
    echo ✅ Virtual environment activated
) else (
    echo ❌ Failed to activate virtual environment
    pause
    exit /b 1
)

REM Upgrade pip in virtual environment
echo ⬆️  Upgrading pip...
python -m pip install --upgrade pip

REM Install dependencies
echo 📦 Installing Python dependencies...
pip install -r requirements.txt

if %errorlevel% equ 0 (
    echo ✅ Dependencies installed successfully
) else (
    echo ❌ Failed to install dependencies
    echo Please check your internet connection and try again
    pause
    exit /b 1
)

REM Download NLTK data
echo 📚 Downloading NLTK data...
python -c "import nltk; print('Downloading punkt...'); nltk.download('punkt'); print('Downloading stopwords...'); nltk.download('stopwords'); print('Downloading wordnet...'); nltk.download('wordnet'); print('✅ NLTK data downloaded successfully')"

if %errorlevel% equ 0 (
    echo ✅ NLTK data downloaded successfully
) else (
    echo ❌ Failed to download NLTK data
    pause
    exit /b 1
)

REM Train Rasa model
echo 🤖 Training Rasa model...
cd rasa_bot
rasa train

if %errorlevel% equ 0 (
    echo ✅ Rasa model trained successfully
    cd ..
) else (
    echo ❌ Failed to train Rasa model
    cd ..
    pause
    exit /b 1
)

REM Create logs directory
if not exist "logs" mkdir logs

echo.
echo 🎉 Setup completed successfully!
echo ================================
echo.
echo 📌 IMPORTANT: Remember to activate the virtual environment before running services:
echo    call venv\Scripts\activate.bat
echo.
echo 🚀 Quick Start:
echo    Windows:     scripts\start_services.bat
echo    Linux/macOS: ./scripts/start_services.sh
echo.
echo 📊 Check Status:
echo    Windows:     scripts\check_services.bat
echo    Linux/macOS: ./scripts/check_services.sh
echo.
echo 🌐 Access URL: http://localhost:8501
echo.
echo Happy Career Counselling! 🎯
pause
