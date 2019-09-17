@echo off
echo.=======================
echo.手机屏幕滑动
echo.=======================

set /p a=请输入时间（ms）控制滑动快慢：

:one
adb shell input swipe 600 1200 600 600 %a%
ping -n 2 127.0>nul
goto :two

:two
adb shell input swipe 600 1200 600 600 %a%
ping -n 3 127.0>nul
goto :one
