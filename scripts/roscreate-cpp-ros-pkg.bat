ECHO OFF

REM Used to help execute because windows is trivially fixated 
REM on extensions.

set DIR=%~dp0
python %DIR%\roscreate-cpp-pkg %*
