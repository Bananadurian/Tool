@echo off&setlocal enabledelayedexpansion
set /p m=请输入屏幕第一个位置:
set /p n=请输入屏幕第二个位置:

for /f "tokens=1,2,3 delims=," %%i in ("%m%") do (set w1=%%i&set h1=%%j&set t1=%%k)
for /f "tokens=1,2,3 delims=," %%o in ("%n%") do (set w2=%%o&set h2=%%p&set t2=%%q)

echo %w1% %h1% %t1%
echo %w2% %h2% %t2%

:one
adb shell input swipe %w1% %h1% %w2% %h2% %t1%
ping -n 2 127.0>nul
goto :two

:two
adb shell input swipe %w1% %h1% %w2% %h2% %t2%
ping -n 3 127.0>nul
goto :one

pause