@echo off
setlocal EnableExtensions
title Shrek Multi Tools ^| Setup
cd /d "%~dp0"

echo [+] Checking Python 3.11...
py -3.11 --version >nul 2>&1
if errorlevel 1 (
    echo [!] Python 3.11 not found on this machine.
    echo [!] Install it from https://www.python.org/downloads/release/python-3116/
    echo [!] then rerun this script.
    pause
    exit /b 1
)

for /f "tokens=2" %%v in ('py -3.11 --version 2^>nul') do echo [+] Python %%v detected.

if not exist "%~dp0requirements.txt" (
    echo [!] requirements.txt not found in this folder!
    pause
    exit /b 1
)

echo [+] Installing requirements...
py -3.11 -m pip install -r "%~dp0requirements.txt"

if errorlevel 1 (
    echo [!] Some packages failed to install - see output above.
) else (
    echo [+] All requirements installed successfully.
)

pause
endlocal