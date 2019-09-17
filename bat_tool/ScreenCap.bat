@echo off
adb wait-for-device
echo.Is taking a screenshot

adb shell screencap -p /sdcard/screen.png
adb pull /sdcard/screen.png C:\Users\Administrator\Desktop
adb shell rm /sdcard/screen.png

pause