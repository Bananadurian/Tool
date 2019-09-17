@echo off
echo.Clearning the Lieyou cache

adb wait-for-device
adb shell pm clear com.feiteng.lieyou

pause