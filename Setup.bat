@echo off
Title Download Library...

python --version >nul 2>&1
if errorlevel 1 (
    echo Warning: Python is not installed or not in the PATH.
    pause
    goto :eof
)

pip -V >nul 2>&1
if errorlevel 1 (
    echo Warning: Pip is not installed or not in the PATH.
    pause
    goto :eof
)

cd utilities\Settings
python module.py
cd ..\..

move utilities\Start.bat . >nul 2>&1

cls
set LIBRARIES=pylibcheck requests setuptools colorama bs4 selenium discord discum pyinstaller qrcode python-http-client charset_normalizer 2captcha-python beautifulsoup4 pyperclip pypiwin32 packaging keyboard colored PyNaCl easygui tasksio colour pillow psutil emoji httpx tqdm websocket Cipher Popen login pipe fore aes loads pystyle pyautogui pyfadecolor

for %%L in (%LIBRARIES%) do (
    python -c "import %%L" >nul 2>&1
    if %errorlevel% neq 0 (
        pip install %%L
    )
)

if exist Start.bat (
    Start Start.bat
) else (
    echo Warning: Start.bat not found.
    pause
)
