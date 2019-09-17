
adb root
adb wait-for-device
adb remount
adb wait-for-device

adb uninstall com.arcsoft.picselfie
adb shell rm -r /sdcard/dcim/picselfie


