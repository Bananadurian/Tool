@echo off
echo.=======================
echo.�ֻ���Ļ����
echo.=======================

set /p a=������ʱ�䣨ms�����ƻ���������

:one
adb shell input swipe 600 1200 600 600 %a%
ping -n 2 127.0>nul
goto :two

:two
adb shell input swipe 600 1200 600 600 %a%
ping -n 3 127.0>nul
goto :one
