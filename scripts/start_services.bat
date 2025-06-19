@echo off
REM AI Virtual Career Counsellor - Service Startup Script (Windows)
REM This script starts all required services for the application

REM Change to the project root directory (parent of scripts folder)
cd /d "%~dp0\.."

echo 🎯 Starting AI Virtual Career Counsellor Services...
echo ==================================================

REM Check if virtual environment exists and activate it
if exist "venv" (
    echo 🔄 Activating virtual environment...
    call venv\Scripts\activate.bat
    echo ✅ Virtual environment activated
) else (
    echo ⚠️  No virtual environment found. Running with system Python.
    echo 💡 Run 'scripts\setup.bat' to create a virtual environment.
)

REM Check if required directories exist
if not exist "rasa_bot" (
    echo ❌ Error: rasa_bot directory not found!
    echo Make sure you're running this script from the project root directory.
    pause
    exit /b 1
)

if not exist "streamlit_app" (
    echo ❌ Error: streamlit_app directory not found!
    pause
    exit /b 1
)

REM Check if model exists
if not exist "rasa_bot\models\*.tar.gz" (
    echo 📚 No trained model found. Training new model...
    cd rasa_bot
    rasa train
    cd ..
    echo ✅ Model training completed!
)

echo 🚀 Starting services...

REM Create logs directory if it doesn't exist
if not exist "logs" mkdir logs

echo ▶️  Starting Rasa Action Server (Port 5055)...
cd rasa_bot
start "Rasa Action Server" cmd /k "rasa run actions --port 5055"
cd ..

REM Wait for action server to start
timeout /t 3 /nobreak >nul

echo ▶️  Starting Rasa Core Server (Port 5005)...
cd rasa_bot
start "Rasa Core Server" cmd /k "rasa run --enable-api --cors=* --port 5005"
cd ..

REM Wait for Rasa server to start
timeout /t 5 /nobreak >nul

echo ▶️  Starting Streamlit App (Port 8501)...
cd streamlit_app
start "Streamlit App" cmd /k "streamlit run app.py"
cd ..

echo.
echo ✅ All services started successfully!
echo ==================================================
echo 🌐 Access the application at: http://localhost:8501
echo.
echo 📊 Service Status:
echo    • Rasa Action Server: Running in separate window
echo    • Rasa Core Server:   Running in separate window  
echo    • Streamlit App:      Running in separate window
echo.
echo 🛑 To stop all services, close the command windows or run: scripts\stop_services.bat
echo 📊 To check service status, run: scripts\check_services.bat
echo.
echo 🎉 Happy Career Counselling!
pause
