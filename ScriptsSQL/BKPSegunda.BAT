@echo off
setlocal enabledelayedexpansion

set "backup_dir=C:\BKP_1.2\Backup\Segunda"
for /f "tokens=1* delims==" %%a in (C:\BKP_1.2\Scripts\server.ini) do (
    if "%%a"=="server" set "server=%%b"
    if "%%a"=="user" set "user=%%b"
    if "%%a"=="password" set "password=%%b"
)

for /f "usebackq tokens=1" %%d in (`sqlcmd -S !server! -U !user! -P !password! -Q "EXEC sp_databases" -h-1`) do (
    set "db_name=%%d"
    if /i not "!db_name!"=="master" if /i not "!db_name!"=="tempdb" if /i not "!db_name!"=="model" if /i not "!db_name!"=="msdb" if /i not "!db_name!"=="ReportServer" if /i not "!db_name!"=="ReportServerTempDB" (
        set "backup_file=!backup_dir!\BKPSegunda_!db_name!.bak"

        echo Realizando backup do banco de dados !db_name!...
        sqlcmd -S !server! -U !user! -P !password! -Q "BACKUP DATABASE [!db_name!] TO DISK='!backup_file!' WITH FORMAT"

        echo Backup do banco de dados !db_name! concluido: !backup_file!
        echo.
    )
)

echo Compactando arquivos .bak em Segunda.zip...
cd "C:\BKP_1.2\Backup\Segunda"
"C:\Program Files\7-Zip\7z.exe" a -tzip "C:\BKP_1.2\Backup\Segunda\Segunda.zip" "*.bak"
copy "C:\BKP_1.2\Backup\Segunda\Segunda.zip" "C:\Program Files (x86)\12informatica\BackupDrive\Segunda"

echo.

echo Apagando arquivos .bak...
del "%backup_dir%\*.bak"

echo.

set "backupFile=C:\BKP_1.2\Backup\Segunda"
set "targetFolder=BackupDrive"

for %%d in (D E F G H I J K L M N O P Q R S T U V W X Y Z) do (
    set "drive=%%d:"
    if exist !drive!\%targetFolder% (
        xcopy /y "%backupFile%" "!drive!\%targetFolder%\"
        if not errorlevel 1 (
            echo Arquivo copiado para !drive!\%targetFolder%.
            exit /b
        )
    )
)

echo Nenhum pendrive encontrado com a pasta %targetFolder%.

echo.

echo Todos os backups foram concluidos.

echo.

endlocal