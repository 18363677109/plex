:: NUKE

:: Hide Commands
:: @echo off

set "newDir=%~dp0\..\data"
python %newDir%\pipeline.py %1 --script software --software nuke

:: exit

