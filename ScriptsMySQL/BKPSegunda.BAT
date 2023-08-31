@echo off
setlocal enabledelayedexpansion

cd "C:\Program Files (x86)\MySQL\MySQL Server 5.1\bin"

set "backup_dir=C:\BKP_1.2\Backup\Segunda"

set "host=localhost"
set "user=root"
set "password=ADMIN"

for /f "usebackq" %%d in (`mysql -h %host% -u %user% -p%password% -e "SHOW DATABASES;"`) do (
  if /i not "%%d"=="information_schema" if /i not "%%d"=="mysql" if /i not "%%d"=="performance_schema" if /i not "%%d"=="database" if /i not "%%d"=="test" (
    set "backup_file=%backup_dir%\BKPSegunda_%%d.sql"

    echo Realizando backup do banco de dados %%d...
	
    mysqldump -h %host% -u %user% -p%password% "%%d" > "!backup_file!"

    echo Backup do banco de dados %%d concluido: !backup_file!
    echo.
  )
)

echo Compactando arquivos .sql em Segunda.zip...
cd "C:\BKP_1.2\Backup\Segunda"
"C:\Program Files\7-Zip\7z.exe" a -tzip "C:\BKP_1.2\Backup\Segunda\Segunda.zip" "*.sql"
copy "C:\BKP_1.2\Backup\Segunda\Segunda.zip" "C:\Program Files (x86)\12informatica\BackupDrive\Segunda"

echo.

echo Apagando arquivos .sql...
del "%backup_dir%\*.sql"

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