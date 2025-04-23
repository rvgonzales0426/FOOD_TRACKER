@echo off
echo Checking current git user configuration...
git config --global user.name
git config --global user.email

echo.
echo Unsetting global git credential helper...
git config --global --unset credential.helper

echo.
echo Clearing git credential cache...
git credential-cache exit

echo.
echo GitHub logout steps completed.
echo If you want to fully remove credentials, consider removing them from Windows Credential Manager manually.
pause
