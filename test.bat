@echo off
setlocal enabledelayedexpansion

for /l %%i in (1,1,100) do (
    set "num=%%i"
    if %%i lss 10 set "num=0!num!"
    md "Day-!num!"
)
