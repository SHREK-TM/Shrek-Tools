@echo off
setlocal

title Shrek Multi Tools ^| PRESS ENTRE

:: Verifie si on a deja les droits admin
net session >nul 2>&1
if %errorLevel% == 0 goto :admin

:: Pas admin -> on se relance soi-meme avec elevation (popup UAC), puis on s'arrete ici
powershell -Command "Start-Process '%~f0' -Verb RunAs"
exit /b

:admin
cd /d "%~dp0"
py -3.11 "Menu.py"
pause
endlocal