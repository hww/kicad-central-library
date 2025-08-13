@echo off
setlocal EnableDelayedExpansion

:: Define all libraries as a space-separated list
:: #set GPLMLIBS=ana cap con cpd dio ics ind mpu mcu pwr rfm res reg xtr osc opt art swi
set GPLMLIBS=audio filter oscillator  fpga resistor capacitor ic rf circuit_protection inductor sensor connector led switch diode mechanical testpoint display memory transformer documentation optics transistor


:: Path to the SQLite database file
set DBFILE=.\database\databook.sqlite

:: Function to create the parts database
:parts_db_create
for %%L in (%GPLMLIBS%) do (
    echo Processing library %%L...
    sqlite3 %DBFILE% "DROP TABLE IF EXISTS %%L"
    if !ERRORLEVEL! neq 0 (
        echo Failed to drop table %%L
        exit /b 1
    )
    sqlite3 -csv %DBFILE% ".import .\\database\\%%L.csv %%L"
    if !ERRORLEVEL! neq 0 (
        echo Failed to import CSV for %%L
        exit /b 1
    )
)
exit /b 0

:: Main script (uncomment to run a specific function)
call :parts_db_create
:: call :parts_db_watch
:: call :parts_db_edit

endlocal
exit /b 0