@echo off
REM AI Virtual Career Counsellor - Service Status Check Script (Windows)
REM This script checks the status of all services

REM Change to the project root directory (parent of scripts folder)
cd /d "%~dp0\.."

echo 📊 AI Virtual Career Counsellor - Service Status
echo ==============================================

echo 🔍 Checking service ports...
echo.

set action_status=0
set rasa_status=0
set streamlit_status=0

REM Check Rasa Action Server (Port 5055)
netstat -an | find ":5055" >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Rasa Action Server is running on port 5055
    set action_status=1
) else (
    echo ❌ Rasa Action Server is NOT running on port 5055
)

REM Check Rasa Core Server (Port 5005)
netstat -an | find ":5005" >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Rasa Core Server is running on port 5005
    set rasa_status=1
) else (
    echo ❌ Rasa Core Server is NOT running on port 5005
)

REM Check Streamlit App (Port 8501)
netstat -an | find ":8501" >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Streamlit App is running on port 8501
    set streamlit_status=1
) else (
    echo ❌ Streamlit App is NOT running on port 8501
)

echo.
echo 📋 Service Summary:
echo ==================

set /a total_running=%action_status%+%rasa_status%+%streamlit_status%

if %total_running% equ 3 (
    echo 🎉 All services are running correctly!
    echo 🌐 Access the application at: http://localhost:8501
) else if %total_running% equ 0 (
    echo ⚠️  No services are running!
    echo 💡 Run 'scripts\start_services.bat' to start all services
) else (
    echo ⚠️  Only %total_running% out of 3 services are running
    echo 💡 You may need to restart services with 'scripts\start_services.bat'
)

echo.
echo 📁 Log Files (if available):
if exist "logs" (
    for %%f in (logs\*.log) do (
        for /f %%i in ('find /c /v "" ^< "%%f"') do echo    📄 %%~nxf: %%i lines
    )
) else (
    echo    ⚠️  No logs directory found
)

echo.
echo 🔧 Useful Commands:
echo    • Start services: scripts\start_services.bat
echo    • Stop services:  scripts\stop_services.bat
echo    • Check ports:    netstat -an ^| find ":5005\|:5055\|:8501"
echo    • Task Manager:   taskmgr
pause
