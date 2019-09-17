@echo off
::adb shell input swipe 900 1000 700 1000

:one
adb shell input swipe 600 1200 600 600 100
ping -n 2 127.0>nul
goto :two

:two
adb shell input swipe 600 1200 300 1200 100
ping -n 3 127.0>nul
goto :three

:three
adb shell input swipe 300 1200 600 1200 100
ping -n 3 127.0>nul
goto :one
