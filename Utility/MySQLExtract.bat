@echo off

set "server=localhost"
set "username=root"
set "password=ADMIN"

echo.

cd "C:\Program Files (x86)\MySQL\MySQL Server 5.1\bin"

for %%A in (comercio comercio1 industria industria1) do (
    echo Verificando o banco de dados %%A...
    mysql -u %username% -p%password% -e "USE %%A; SELECT COUNT(*) FROM information_schema.tables WHERE table_schema = '%%A' AND table_name = 'empresa';" | findstr /r /c:"1"
    if %errorlevel%==0 (
        set "dbname=%%A"
        goto :query_data
    )
)

echo A tabela "empresa" nao foi encontrada em nenhum dos bancos de dados especificados.
goto :end

:query_data
mysql -u %username% -p%password% -D %dbname% -e "SELECT EmpNom, EmpNomFan, EmpCnpj, EmpVerSis, EmpVctCert FROM empresa" > "C:\BKP_1.2\Empresa.txt"
echo As informacoes foram extraidas com sucesso e salvas no arquivo Empresa.txt.

echo.

:end
endlocal