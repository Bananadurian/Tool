@echo off
adb wait-for-device
echo.uninstall lieyou

adb uninstall com.feiteng.lieyou
pause