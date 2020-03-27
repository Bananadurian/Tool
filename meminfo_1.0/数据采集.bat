@echo off
if EXIST dump_meminfo.txt del dump_meminfo.txt
python dump_meminfo.py
pause