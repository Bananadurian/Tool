@echo off
echo. Screenrecord now
adb wait-for-device
adb shell screenrecord --time-limit 15 /sdcard/demo.mp4
echo. Pull file
adb pull /sdcard/demo.mp4 C:\Users\Administrator\Desktop
adb shell rm /sdcard/demo.mp4
pause

rem --time-limit 指定时间，默认180s --size 默认手机尺寸