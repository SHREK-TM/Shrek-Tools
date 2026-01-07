@echo off
title Python 3.11 Verification and Library Installation
cls

echo ==========================================
echo   Checking for Python 3.11
echo ==========================================

REM Check if Python 3.11 is installed
py -3.11 --version >nul 2>&1
if errorlevel 1 (
    echo.
    echo [ERROR] Python 3.11 is not installed on this system.
    echo Please install Python 3.11 and run this script again.
    echo https://www.python.org/downloads/release/python-3110/
    echo.
    pause
    exit /b
)

echo Python 3.11 detected successfully.
echo.

REM Force Python 3.11 usage
set PYTHON=py -3.11

echo ==========================================
echo   Installing required libraries
echo ==========================================

set LIBRARIES=setuptools==65.5.0 pip==22.3.1 wheel requests==2.26.0 colorama selenium==4.0.0 discord.py==2.3.2 pyinstaller qrcode python-http-client charset_normalizer==2.0.10 2captcha-python beautifulsoup4 pyperclip pypiwin32 packaging keyboard colored PyNaCl easygui tasksio colour pillow psutil emoji httpx tqdm websocket-client pystyle pyautogui pylibcheck

for %%L in (%LIBRARIES%) do (
    echo Installing %%L ...
    %PYTHON% -m pip install "%%L" --upgrade --quiet
)
(
    echo @echo off
    echo py -3.11 "Menu.py"
    echo pause
) > Start.bat

if exist Start.bat (
    start cmd /k Start.bat
) else (
    echo [WARNING] Failed to create Start.bat.
)

pause
