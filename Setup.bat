@echo off
Title Download Modules...
python --version 3>NUL
if errorlevel 1 goto errorNoPython
pip -v>NUL
if errorlevel 1 goto errorNoPip
python -m pip install -r requirements.txt
move utilities\Start.bat .
cd utilities\Settings
cd ..
cd ..
cls
Start.bat
