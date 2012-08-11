@ECHO OFF

set PWD=%~dp0
set COMMAND=%1
if X%COMMAND%==X set COMMAND=all
if X%COMMAND%==Xhelp goto Help
if X%COMMAND%==Xclean goto Clean
if X%COMMAND%==Xall goto Distro
if X%COMMAND%==Xdistro goto Distro
if X%COMMAND%==Xupload goto Upload
if X%COMMAND%==Xinstall goto Install
if X%COMMAND%==Xuninstall goto UnInstall
goto Help

:Help
echo "Usage: call with args from ['clean', 'all', 'distro', 'upload', 'install', 'uninstall']"
goto End

:Distro
echo.
echo "Building msi installer."
python setup.py bdist_msi
cd ..
if X%COMMAND%==Xall (
  goto Upload
) else (
  goto End
)

:Upload
echo.
echo "Uploading to file server."
cd dist
scp *.msi files@files.yujinrobot.com:pub/appupdater/python/2.7/
cd ..\..
goto End

:Install
python setup.py install --record install.record
goto End

:UnInstall
goto End

:Clean
rd /S /Q %cd%\build
rd /S /Q %cd%\dist
rm MANIFEST
goto End

:End
cd %PWD%