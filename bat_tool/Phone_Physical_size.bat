@echo off 
echo.The phone physical screen size
adb wait-for-device
adb shell wm size

pause