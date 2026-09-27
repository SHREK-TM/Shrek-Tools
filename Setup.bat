@echo off
setlocal EnableExtensions
title Shrek Multi Tools ^| Setup
cd /d "%~dp0"

cls

:: Détection de l'architecture Windows
set "ARCH=x64"
if "%PROCESSOR_ARCHITECTURE%"=="x86" set "ARCH=x86"
if "%PROCESSOR_ARCHITEW6432%"=="AMD64" set "ARCH=x64"

powershell -Command "Write-Host '[' -ForegroundColor Green -NoNewline; Write-Host '+' -ForegroundColor White -NoNewline; Write-Host ']' -ForegroundColor Green -NoNewline; Write-Host ' Detection de l architecture Windows : %ARCH%'"

:: Vérification de la présence de Python 3.11
py -3.11 --version >nul 2>&1
if errorlevel 1 (
    powershell -Command "Write-Host '[' -ForegroundColor Red -NoNewline; Write-Host '!' -ForegroundColor White -NoNewline; Write-Host ']' -ForegroundColor Red -NoNewline; Write-Host ' Python 3.11 n a pas ete trouve sur cette machine !'"
    powershell -Command "Write-Host '[' -ForegroundColor Yellow -NoNewline; Write-Host '!' -ForegroundColor White -NoNewline; Write-Host ']' -ForegroundColor Yellow -NoNewline; Write-Host ' Veuillez l installer depuis : https://www.python.org/downloads/release/python-3116/'"
    powershell -Command "Write-Host '[' -ForegroundColor Yellow -NoNewline; Write-Host '!' -ForegroundColor White -NoNewline; Write-Host ']' -ForegroundColor Yellow -NoNewline; Write-Host ' Cochez bien \"Add Python to PATH\" lors de l installation, puis relancez ce script.'"
    pause
    exit /b 1
)

for /f "tokens=2" %%v in ('py -3.11 --version 2^>nul') do (
    powershell -Command "Write-Host '[' -ForegroundColor Green -NoNewline; Write-Host '+' -ForegroundColor White -NoNewline; Write-Host ']' -ForegroundColor Green -NoNewline; Write-Host ' Python %%v detecte avec succes.'"
)

:: Génération du fichier requirements.txt
powershell -Command "Write-Host '[' -ForegroundColor Green -NoNewline; Write-Host '+' -ForegroundColor White -NoNewline; Write-Host ']' -ForegroundColor Green -NoNewline; Write-Host ' Verification / Creation de requirements.txt...'"

(
    echo # --- Pip / build ---
    echo setuptools==65.5.0
    echo wheel==0.42.0
    echo pip==24.0
    echo.
    echo # --- Core HTTP ---
    echo requests==2.31.0
    echo charset-normalizer==3.3.2
    echo packaging==23.2
    echo aiohttp==3.9.5
    echo httpx==0.28.1
    echo websocket-client==0.59.0
    echo.
    echo # --- Discord ---
    echo discord.py==2.3.2
    echo discum==1.4.1
    echo PyNaCl==1.5.0
    echo discord-interactions==0.4.0
    echo.
    echo # --- Web / scraping ---
    echo selenium==4.15.2
    echo beautifulsoup4==4.12.2
    echo webdriver-manager==4.0.1
    echo.
    echo # --- Console / UI ---
    echo colorama==0.4.6
    echo customtkinter==5.2.2
    echo pystyle==2.9
    echo colored==2.2.3
    echo easygui==0.98.3
    echo rich==13.7.1
    echo pystray==0.19.5
    echo.
    echo # --- Image / media ---
    echo Pillow==10.1.0
    echo qrcode==7.4.2
    echo edge-tts==6.1.12
    echo mss==9.0.1
    echo numpy==1.26.4
    echo opencv-python==4.10.0.84
    echo pycaw==20240210
    echo pygetwindow==0.0.9
    echo screen-brightness-control==0.15.0
    echo geocoder==1.38.1
    echo pyaudio==0.2.14
    echo.
    echo # --- Windows / system ---
    echo pywin32==306
    echo pyautogui==0.9.54
    echo keyboard==0.13.5
    echo psutil==5.9.6
    echo pynput==1.7.7
    echo send2trash==1.8.3
    echo.
    echo # --- Crypto / security ---
    echo cryptography==42.0.8
    echo pycryptodome==3.20.0
    echo pycryptodomex==3.20.0
    echo argon2-cffi==23.1.0
    echo.
    echo # --- Network / scan ---
    echo scapy==2.5.0
    echo phonenumbers==8.13.40
    echo.
    echo # --- Build / misc ---
    echo pyinstaller==6.1.0
    echo python-http-client==3.3.7
    echo 2captcha-python==1.1.3
    echo emoji==2.8.0
    echo pylibcheck==0.2.2
    echo pyperclip==1.8.2
    echo colour==0.1.5
    echo tqdm==4.66.1
    echo reportlab==4.2.2
    echo keyauth==1.0.3
) > "%~dp0requirements.txt"

:: Installation des dépendances
powershell -Command "Write-Host '[' -ForegroundColor Green -NoNewline; Write-Host '+' -ForegroundColor White -NoNewline; Write-Host ']' -ForegroundColor Green -NoNewline; Write-Host ' Installation des bibliotheques via pip...'"

py -3.11 -m pip install -r "%~dp0requirements.txt" --quiet

if errorlevel 1 (
    powershell -Command "Write-Host '[' -ForegroundColor Yellow -NoNewline; Write-Host '!' -ForegroundColor White -NoNewline; Write-Host ']' -ForegroundColor Yellow -NoNewline; Write-Host ' Certaines bibliotheques ont echoue lors de l installation. Verifiez la sortie ci-dessus.'"
) else (
    powershell -Command "Write-Host '[' -ForegroundColor Green -NoNewline; Write-Host '+' -ForegroundColor White -NoNewline; Write-Host ']' -ForegroundColor Green -NoNewline; Write-Host ' Toutes les bibliotheques ont ete installees avec succes.'"
)

:: Génération du fichier Start.bat avec élévation Admin (UAC)
(
    echo @echo off
    echo setlocal
    echo.
    echo title Shrek Multi Tools ^^| PRESS ENTRE
    echo.
    echo net session ^>nul 2^>^&1
    echo if %%errorLevel%% == 0 goto :admin
    echo.
    echo powershell -Command "Start-Process '%%~f0' -Verb RunAs"
    echo exit /b
    echo.
    echo :admin
    echo cd /d "%%~dp0"
    echo py -3.11 "Menu.py"
    echo pause
    echo endlocal
) > "%~dp0Start.bat"

powershell -Command "Write-Host '[' -ForegroundColor Green -NoNewline; Write-Host '+' -ForegroundColor White -NoNewline; Write-Host ']' -ForegroundColor Green -NoNewline; Write-Host ' Start.bat cree avec succes.'"

:: Lancement du projet et des ressources
start cmd /k "%~dp0Start.bat"
start https://github.com/SHREK-TM/Shrek-Tools

if exist "%~dp0input\Star.png" (
    start "" "%~dp0input\star.png"
)

pause
endlocal
