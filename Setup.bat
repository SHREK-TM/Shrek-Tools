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

    powershell -Command "(New-Object Net.WebClient).DownloadFile('%PY_URL%', 'python_installer.exe')"
    python_installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_tcltk=1

    if errorlevel 1 (
        powershell -Command "Write-Host '[' -ForegroundColor Red -NoNewline; Write-Host '!' -ForegroundColor White -NoNewline; Write-Host ']' -ForegroundColor Red -NoNewline; Write-Host ' Python install failed!'"
        pause & exit /b 1
    )

    py -3.11 -m ensurepip --upgrade
)

powershell -Command "Write-Host '[' -ForegroundColor Green -NoNewline; Write-Host '+' -ForegroundColor White -NoNewline; Write-Host ']' -ForegroundColor Green -NoNewline; Write-Host ' Python 3.11.6 detected or installed successfully.'"

:: Create requirements.txt with pinned compatible versions
powershell -Command "Write-Host '[' -ForegroundColor Green -NoNewline; Write-Host '+' -ForegroundColor White -NoNewline; Write-Host ']' -ForegroundColor Green -NoNewline; Write-Host ' Creating requirements.txt...'"

(
    echo setuptools==65.5.0
    echo pip==23.3.1
    echo wheel==0.41.3
    echo requests==2.31.0
    echo colorama==0.4.6
    echo selenium==4.15.2
    echo discord.py==2.3.2
    echo pyinstaller==6.1.0
    echo qrcode==7.4.2
    echo python-http-client==3.3.7
    echo charset-normalizer==3.3.2
    echo 2captcha-python==1.1.3
    echo emoji==2.8.0
    echo beautifulsoup4==4.12.2
    echo pylibcheck==0.2.2
    echo pyperclip==1.8.2
    echo pypiwin32==223
    echo packaging==23.2
    echo keyboard==0.13.5
    echo colored==2.2.3
    echo PyNaCl==1.5.0
    echo easygui==0.98.3
    echo colour==0.1.5
    echo Pillow==10.1.0
    echo psutil==5.9.6
    echo httpx==0.28.1
    echo tqdm==4.66.1
    echo websocket-client==1.8.0
    echo webdriver-manager==4.0.1
    echo pystyle==2.9
    echo pyautogui==0.9.54
) > requirements.txt

powershell -Command "Write-Host '[' -ForegroundColor Green -NoNewline; Write-Host '+' -ForegroundColor White -NoNewline; Write-Host ']' -ForegroundColor Green -NoNewline; Write-Host ' Installing all libraries...'"

py -3.11 -m pip install -r requirements.txt --quiet

if errorlevel 1 (
    powershell -Command "Write-Host '[' -ForegroundColor Yellow -NoNewline; Write-Host '!' -ForegroundColor White -NoNewline; Write-Host ']' -ForegroundColor Yellow -NoNewline; Write-Host ' Some libraries may have failed, check output above.'"
) else (
    powershell -Command "Write-Host '[' -ForegroundColor Green -NoNewline; Write-Host '+' -ForegroundColor White -NoNewline; Write-Host ']' -ForegroundColor Green -NoNewline; Write-Host ' All libraries installed successfully.'"
)

(
    echo @echo off
    echo py -3.11 "Menu.py"
    echo pause
) > Start.bat

powershell -Command "Write-Host '[' -ForegroundColor Green -NoNewline; Write-Host '+' -ForegroundColor White -NoNewline; Write-Host ']' -ForegroundColor Green -NoNewline; Write-Host ' Start.bat created successfully.'"

start cmd /k Start.bat
pause
