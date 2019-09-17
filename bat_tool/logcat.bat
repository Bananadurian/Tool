@echo off
echo.Printing log
adb wait-for-device
adb logcat -c
adb logcat >C:\Users\Administrator\Desktop\Crash_log_20190214.txt
