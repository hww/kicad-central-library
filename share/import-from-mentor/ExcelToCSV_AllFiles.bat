# windows command line
# used for converting .xlsx files to .csv files
FOR /f "delims=" %%i IN ('DIR *.xlsx /b') DO ExcelToCSV.vbs "%%i" "%%i.csv"
