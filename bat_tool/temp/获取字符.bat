@echo off
set /p a=please input number:

for /f "tokens=1-3 delims=," %%i in ("%a%") do echo %%i %%j %%k 

pause