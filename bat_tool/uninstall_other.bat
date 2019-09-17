:loop
@echo off&color 07
echo. ================================
echo. 卸载APP
echo. ================================
echo. 1：卸载爱拍
echo. 2：卸载拍大师
echo. 3：卸载猎游
echo. 命令执行后按任意键退出
echo. ================================

adb wait-for-device
adb devices
::pause

set /p a=请输入命令并回车,退出按"Q":
 
if "%a%"=="1" goto :1
if "%a%"=="2" goto :2
if "%a%"=="3" goto :3
if "%a%"=="4" goto :4
if /i "%a%"=="q" goto :end
 
color 84
cls&echo,&echo, 输入错误请核对
echo,&echo, 你输入的是【%a%】
echo,&echo, 注意大小写,请三秒后重试!。
ping -n 5 127.1>nul
cls&goto :loop
 
:1 
adb uninstall com.aipai.android
pause>nul
goto :end
 
:2
adb uninstall com.aipai.paidashi
pause>nul
goto :end

:3
adb uninstall com.feiteng.lieyou
pause>nul
goto :end

:4
set /p b=安装包路径：
adb install -r %b%
pause>nul
goto :end

:end
exit