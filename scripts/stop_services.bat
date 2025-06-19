@echo off
REM AI Virtual Career Counsellor - Service Stop Script (Windows)
REM This script stops all running services

REM Change to the project root directory (parent of scripts folder)
cd /d "%~dp0\.."

echo 🛑 Stopping AI Virtual Career Counsellor Services...
echo ==================================================

echo 🔍 Stopping Rasa Action Server...
taskkill /f /im cmd.exe /fi "WINDOWTITLE eq Rasa Action Server*" >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Rasa Action Server stopped
) else (
    echo ⚠️  Rasa Action Server was not running
)

echo 🔍 Stopping Rasa Core Server...
taskkill /f /im cmd.exe /fi "WINDOWTITLE eq Rasa Core Server*" >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Rasa Core Server stopped
) else (
    echo ⚠️  Rasa Core Server was not running
)

echo 🔍 Stopping Streamlit App...
taskkill /f /im cmd.exe /fi "WINDOWTITLE eq Streamlit App*" >nul 2>&1
if %errorlevel% equ 0 (
    echo ✅ Streamlit App stopped
) else (
    echo ⚠️  Streamlit App was not running
)

REM Also try to kill processes by name
echo 🔍 Stopping any remaining processes...
taskkill /f /im python.exe /fi "COMMANDLINE eq *rasa*" >nul 2>&1
taskkill /f /im python.exe /fi "COMMANDLINE eq *streamlit*" >nul 2>&1

echo.
echo ✅ All services stopped successfully!
echo 🔍 To verify, check Task Manager for any remaining Python processes
pause
