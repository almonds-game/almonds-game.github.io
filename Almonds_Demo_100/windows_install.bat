@ECHO OFF

del *unix*
echo Current directory: %CD%

echo Installing libraries...
pip3 install -r requirements.txt


echo Moving folders around...
cd ..
echo Current directory: %CD%
move Almonds_Demo $env:USERPROFILE\Downloads

pause