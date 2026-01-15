@echo off
title Python 3.11.6 Verification and Library Installation
cls

powershell -Command "Write-Host '[' -ForegroundColor Green -NoNewline; Write-Host '+' -ForegroundColor White -NoNewline; Write-Host ']' -ForegroundColor Green -NoNewline; Write-Host ' Checking for Python 3.11.6'"

for /f "tokens=2" %%v in ('py -3.11 --version 2^>nul') do set "PY_VER=%%v"
if "%PY_VER%" neq "3.11.6" (
    echo.
    powershell -Command "Write-Host '[' -ForegroundColor Red -NoNewline; Write-Host 'ERROR' -ForegroundColor White -NoNewline; Write-Host ']' -ForegroundColor Red -NoNewline; Write-Host ' Python 3.11.6 is not installed on this system.'"
    powershell -Command "Write-Host '[' -ForegroundColor Green -NoNewline; Write-Host '+' -ForegroundColor White -NoNewline; Write-Host ']' -ForegroundColor Green -NoNewline; Write-Host ' Please install Python 3.11.6 and run this script again.'"
    powershell -Command "Write-Host '[' -ForegroundColor Green -NoNewline; Write-Host '+' -ForegroundColor White -NoNewline; Write-Host ']' -ForegroundColor Green -NoNewline; Write-Host ' https://www.python.org/downloads/release/python-3116/'"
    echo.
    pause
    exit /b
)

powershell -Command "Write-Host '[' -ForegroundColor Green -NoNewline; Write-Host '+' -ForegroundColor White -NoNewline; Write-Host ']' -ForegroundColor Green -NoNewline; Write-Host ' Python 3.11.6 detected successfully.'"

set PYTHON=py -3.11

powershell -Command "Write-Host '[' -ForegroundColor Green -NoNewline; Write-Host '+' -ForegroundColor White -NoNewline; Write-Host ']' -ForegroundColor Green -NoNewline; Write-Host ' Installing required libraries'"

set LIBRARIES=setuptools==65.5.0 pip==22.3.1 wheel requests==2.26.0 colorama selenium==4.0.0 discord.py==2.3.2 pyinstaller qrcode python-http-client charset_normalizer==2.0.10 2captcha-python beautifulsoup4 pylibcheck pyperclip pypiwin32 packaging keyboard colored PyNaCl easygui tasksio colour pillow psutil emoji httpx tqdm websocket-client pystyle pyautogui pylibcheck

for %%L in (%LIBRARIES%) do (
    powershell -Command "Write-Host '[' -ForegroundColor Green -NoNewline; Write-Host '+' -ForegroundColor White -NoNewline; Write-Host ']' -ForegroundColor Green -NoNewline; Write-Host ' Installing %%L ...'"
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
    powershell -Command "Write-Host '[' -ForegroundColor Red -NoNewline; Write-Host 'WARNING' -ForegroundColor White -NoNewline; Write-Host ']' -ForegroundColor Red -NoNewline; Write-Host ' Failed to create Start.bat.'"
)

pause

