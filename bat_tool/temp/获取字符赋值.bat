@echo off&setlocal enabledelayedexpansion
set /p m=��������Ļ��һ��λ��:
set /p n=��������Ļ�ڶ���λ��:

for /f "tokens=1,2,3 delims=," %%i in ("%m%") do (set w1=%%i&set h1=%%j&set t1=%%k)
for /f "tokens=1,2,3 delims=," %%o in ("%n%") do (set w2=%%o&set h2=%%p&set t2=%%q)

echo %w1% %h1% %t1%
echo %w2% %h2% %t2%
pause