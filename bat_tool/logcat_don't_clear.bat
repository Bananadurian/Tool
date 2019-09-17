@echo off
echo.Printing log
adb wait-for-device
adb logcat >C:\Users\Administrator\Desktop\Crash_log_20190326.txt
