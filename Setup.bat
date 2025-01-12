@echo off
Title Download Library...

:: Vérification si Python est dans le PATH
where python >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not added to PATH.
    set /p choice=Do you want to add Python to PATH? (Y/N): 
    if /i "%choice%"=="Y" (
        :: Recherche du chemin d'installation de Python
        for /f "tokens=2*" %%a in ('reg query "HKCU\Software\Python\PythonCore" /s /v "InstallPath" 2^>nul ^| find "InstallPath"') do (
            set PYTHON_PATH=%%b
        )
        if not defined PYTHON_PATH (
            for /f "tokens=2*" %%a in ('reg query "HKLM\Software\Python\PythonCore" /s /v "InstallPath" 2^>nul ^| find "InstallPath"') do (
                set PYTHON_PATH=%%b
            )
        )

        if defined PYTHON_PATH (
            echo Adding Python to PATH...
            setx PATH "%PATH%;%PYTHON_PATH%"
            echo Python has been added to PATH. Please restart the script.
        ) else (
            echo Python installation not found. Please reinstall Python and select "Add to PATH".
        )
        pause
        goto :eof
    ) else (
        echo Python is required in PATH to continue.
        pause
        goto :eof
    )
)

:: Vérification de la version de Python
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

:: Vérification si pip est installé
pip -V >nul 2>&1
if errorlevel 1 (
    echo Error: Pip is not installed or not in the PATH.
    pause
    goto :eof
)

cls
echo Installing required libraries...

:: Liste des bibliothèques Python à installer
set LIBRARIES=setuptools==65.5.0 pip==22.3.1 wheel requests==2.26.0 colorama selenium==4.0.0 discord==2.5.1 pyinstaller qrcode python-http-client charset_normalizer==2.0.10 2captcha-python beautifulsoup4 pyperclip pypiwin32 packaging keyboard colored PyNaCl easygui tasksio colour pillow psutil emoji httpx tqdm websocket Cipher Popen login pipe fore aes loads pystyle pyautogui pyfadecolor

:: Installation des bibliothèques
for %%L in (%LIBRARIES%) do (
    python -m pip install "%%L" --upgrade --quiet
)

:: Création du fichier Start.bat
(
    echo @echo off
    echo Python Menu.py
) > Start.bat

:: Lancement de Start.bat
if exist Start.bat (
    Start Start.bat
) else (
    echo Warning: Start.bat could not be created.
    pause
)
