:: MAYA

:: Hide Commands
@echo off

:: call %~dp0\win_env.bat

set "newDir=%~dp0\..\data"
pythonw %newDir%\pipeline.py %1 --script software --software maya

exit
