:loop
@echo off&color 07
echo. ================================
echo. ж��APP
echo. ================================
echo. 1��ж�ذ���
echo. 2��ж���Ĵ�ʦ
echo. 3��ж������
echo. ����ִ�к�������˳�
echo. ================================

adb wait-for-device
adb devices
::pause

set /p a=����������س�,�˳���"Q":
 
if "%a%"=="1" goto :1
if "%a%"=="2" goto :2
if "%a%"=="3" goto :3
if "%a%"=="4" goto :4
if /i "%a%"=="q" goto :end
 
color 84
cls&echo,&echo, ���������˶�
echo,&echo, ��������ǡ�%a%��
echo,&echo, ע���Сд,�����������!��
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
set /p b=��װ��·����
adb install -r %b%
pause>nul
goto :end

:end
exit