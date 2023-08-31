@echo off
setlocal

set "backupFolder=C:\Program Files (x86)\12informatica\BackupDrive"
set "batPath=C:\BKP_1.2\Scripts\SendEmail.bat"
set "daysThreshold=8"

for /r "%backupFolder%" %%G in (*) do (
  set "file=%%G"
  setlocal enabledelayedexpansion
  for /f %%A in ('powershell -Command "Get-Date -Format yyyyMMdd"') do (
    set "currentDate=%%A"
  )
  for /f %%B in ('powershell -Command "((Get-Date).AddDays(-%daysThreshold%)).ToString('yyyyMMdd')"') do (
    set "thresholdDate=%%B"
  )
  for /f %%C in ('powershell -Command "(Get-Item -Path '!file!').LastWriteTime.ToString('yyyyMMdd')"') do (
    set "fileDate=%%C"
  )
  if !fileDate! LEQ !thresholdDate! (
    echo Executing batch script for file: !file!
    call "%batPath%"
  )
  endlocal
)

endlocal
