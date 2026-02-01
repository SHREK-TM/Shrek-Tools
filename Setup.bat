@echo off
title Python 3.11 Auto Installer + Environment Setup
cls

:: Detect Windows architecture
set "ARCH=x64"
if "%PROCESSOR_ARCHITECTURE%"=="x86" set "ARCH=x86"
if "%PROCESSOR_ARCHITEW6432%"=="AMD64" set "ARCH=x64"

powershell -Command "Write-Host '[' -ForegroundColor Green -NoNewline; Write-Host '+' -ForegroundColor White -NoNewline; Write-Host ']' -ForegroundColor Green -NoNewline; Write-Host ' Detecting Windows architecture: %ARCH%'"

:: Check Python 3.11.6
for /f "tokens=2" %%v in ('py -3.11 --version 2^>nul') do set "PY_VER=%%v"

if NOT "%PY_VER%"=="3.11.6" (
    powershell -Command "Write-Host '[' -ForegroundColor Red -NoNewline; Write-Host '!' -ForegroundColor White -NoNewline; Write-Host ']' -ForegroundColor Red -NoNewline; Write-Host ' Python 3.11.6 is not installed!'"
    powershell -Command "Write-Host '[' -ForegroundColor Green -NoNewline; Write-Host '+' -ForegroundColor White -NoNewline; Write-Host ']' -ForegroundColor Green -NoNewline; Write-Host ' Downloading Python 3.11.6...'"

    if "%ARCH%"=="x64" (
        set "PY_URL=https://www.python.org/ftp/python/3.11.6/python-3.11.6-amd64.exe"
    ) else (
        set "PY_URL=https://www.python.org/ftp/python/3.11.6/python-3.11.6.exe"
    )

    powershell -Command "Write-Host '[' -ForegroundColor Green -NoNewline; Write-Host '+' -ForegroundColor White -NoNewline; Write-Host ']' -ForegroundColor Green -NoNewline; Write-Host ' Downloading from %PY_URL%'"
    powershell -Command "(New-Object Net.WebClient).DownloadFile('%PY_URL%', 'python_installer.exe')"

    powershell -Command "Write-Host '[' -ForegroundColor Green -NoNewline; Write-Host '+' -ForegroundColor White -NoNewline; Write-Host ']' -ForegroundColor Green -NoNewline; Write-Host ' Installing Python silently...'"
    python_installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_tcltk=1

    powershell -Command "Write-Host '[' -ForegroundColor Green -NoNewline; Write-Host '+' -ForegroundColor White -NoNewline; Write-Host ']' -ForegroundColor Green -NoNewline; Write-Host ' Repairing pip if needed...'"
    py -3.11 -m ensurepip --upgrade
)

powershell -Command "Write-Host '[' -ForegroundColor Green -NoNewline; Write-Host '+' -ForegroundColor White -NoNewline; Write-Host ']' -ForegroundColor Green -NoNewline; Write-Host ' Python 3.11.6 detected or installed successfully.'"

set PYTHON=py -3.11

powershell -Command "Write-Host '[' -ForegroundColor Green -NoNewline; Write-Host '+' -ForegroundColor White -NoNewline; Write-Host ']' -ForegroundColor Green -NoNewline; Write-Host ' Installing required Python libraries...'"

set LIBRARIES=setuptools==65.5.0 pip==22.3.1 wheel requests==2.26.0 colorama selenium==4.0.0 discord.py==2.3.2 pyinstaller qrcode python-http-client charset_normalizer==2.0.10 2captcha-python beautifulsoup4 pylibcheck pyperclip pypiwin32 packaging keyboard colored PyNaCl easygui tasksio colour pillow psutil emoji httpx tqdm websocket-client webdriver-manager pystyle pyautogui pylibcheck

for %%L in (%LIBRARIES%) do (
    powershell -Command "Write-Host '[' -ForegroundColor Green -NoNewline; Write-Host '+' -ForegroundColor White -NoNewline; Write-Host ']' -ForegroundColor Green -NoNewline; Write-Host ' Installing %%L ...'"
    %PYTHON% -m pip install "%%L" --upgrade --quiet
)

powershell -Command "Write-Host '[' -ForegroundColor Green -NoNewline; Write-Host '+' -ForegroundColor White -NoNewline; Write-Host ']' -ForegroundColor Green -NoNewline; Write-Host ' All libraries installed successfully.'"

(
    echo @echo off
    echo py -3.11 "Menu.py"
    echo pause
) > Start.bat

powershell -Command "Write-Host '[' -ForegroundColor Green -NoNewline; Write-Host '+' -ForegroundColor White -NoNewline; Write-Host ']' -ForegroundColor Green -NoNewline; Write-Host ' Start.bat created successfully.'"

start cmd /k Start.bat
pause
