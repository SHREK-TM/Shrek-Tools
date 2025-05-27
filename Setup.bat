@echo off
Title Download Library...

cls
echo Installing required libraries...

set LIBRARIES=setuptools==65.5.0 pip==22.3.1 wheel requests==2.26.0 colorama selenium==4.0.0 discord.py==2.3.2 pyinstaller qrcode python-http-client charset_normalizer==2.0.10 2captcha-python beautifulsoup4 pyperclip pypiwin32 packaging keyboard colored PyNaCl easygui tasksio colour pillow psutil emoji httpx tqdm websocket-client pystyle pyautogui pylibcheck

for %%L in (%LIBRARIES%) do (
    python -m pip install "%%L" --upgrade --quiet
)

(
    echo @echo off
    echo python "Menu.py"
    echo pause
) > Start.bat

if exist Start.bat (
    start cmd /k Start.bat
) else (
    echo Warning: Start.bat could not be created.
)
