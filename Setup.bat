@echo off
Title Download Library...

for /f "tokens=2 delims= " %%v in ('python --version 2^>nul') do (
    for /f "tokens=1,2 delims=." %%i in ("%%v") do (
        if %%i lss 3 (
            echo Warning: Python version must be >= 3.11.
            pause
            goto :eof
        )
        if %%i==3 if %%j lss 11 (
            echo Warning: Python version must be >= 3.11.
            pause
            goto :eof
        )
    )
)

where python >nul 2>&1
if errorlevel 1 (
    echo Python is not added to PATH. Please reinstall Python and check "Add to PATH" option.
    pause
    goto :eof
)

pip -V >nul 2>&1
if errorlevel 1 (
    echo Warning: Pip is not installed or not in the PATH.
    pause
    goto :eof
)

cls
set LIBRARIES=setuptools==65.5.0 pip==22.3.1 wheel requests==2.26.0 colorama selenium==4.0.0 discord==2.5.1 pyinstaller qrcode python-http-client charset_normalizer==2.0.10 2captcha-python beautifulsoup4 pyperclip pypiwin32 packaging keyboard colored PyNaCl easygui tasksio colour pillow psutil emoji httpx tqdm websocket Cipher Popen login pipe fore aes loads pystyle pyautogui pyfadecolor

for %%L in (%LIBRARIES%) do (
    python -m pip install "%%L" --upgrade --quiet
)

(
    echo @echo off
    echo Python Menu.py
) > Start.bat

if exist Start.bat (
    Start Start.bat
) else (
    echo Warning: Start.bat could not be created.
    pause
)
