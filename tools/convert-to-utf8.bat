@echo off
REM Convert all non-UTF8 dictionary files to UTF-8
REM Uses iconv.exe from MSYS2
REM
REM Usage: convert-to-utf8.bat
REM
REM Prerequisites:
REM   - MSYS2 installed at C:\msys64
REM   - iconv.exe available at C:\msys64\usr\bin\iconv.exe

setlocal EnableDelayedExpansion

set ICONV="C:\msys64\usr\bin\iconv.exe"
set DICTS_DIR=%~dp0..\dicts

if not exist %ICONV% (
    echo ERROR: iconv.exe not found at %ICONV%
    echo Install MSYS2 or adjust the ICONV path in this script.
    exit /b 1
)

echo ========================================
echo  Converting dictionaries to UTF-8
echo ========================================
echo.

REM Mapping of language codes to their original encodings
REM Format: code:source_encoding
set CONVERSIONS=an:ISO-8859-1 bs:ISO-8859-2 de:ISO-8859-1 el:ISO-8859-7 et:ISO-8859-15 id:ISO-8859-1 lt:ISO-8859-13 no:ISO-8859-1 pl:ISO-8859-2 sl:ISO-8859-2 ar:WINDOWS-1256 pt-BR:ISO-8859-1

for %%C in (%CONVERSIONS%) do (
    for /F "tokens=1,2 delims=:" %%A in ("%%C") do (
        set CODE=%%A
        set SRC_ENC=%%B

        set DICT_DIR=%DICTS_DIR%\dict-!CODE!
        if exist "!DICT_DIR!" (
            echo Converting dict-!CODE! (!SRC_ENC! -> UTF-8)...

            REM Convert .aff file
            for %%F in ("!DICT_DIR!\*.aff") do (
                %ICONV% -f !SRC_ENC! -t UTF-8 "%%F" > "%%F.tmp"
                if errorlevel 1 (
                    echo   WARNING: Failed to convert %%~nxF
                    del "%%F.tmp" 2>nul
                ) else (
                    move /Y "%%F.tmp" "%%F" >nul
                    echo   Converted %%~nxF
                )
            )

            REM Convert .dic file
            for %%F in ("!DICT_DIR!\*.dic") do (
                %ICONV% -f !SRC_ENC! -t UTF-8 "%%F" > "%%F.tmp"
                if errorlevel 1 (
                    echo   WARNING: Failed to convert %%~nxF
                    del "%%F.tmp" 2>nul
                ) else (
                    move /Y "%%F.tmp" "%%F" >nul
                    echo   Converted %%~nxF
                )
            )

            REM Update SET line in .aff to UTF-8
            for %%F in ("!DICT_DIR!\*.aff") do (
                python -u -c "
import sys
path = sys.argv[1]
with open(path, 'r', encoding='utf-8', errors='replace') as f:
    lines = f.readlines()
with open(path, 'w', encoding='utf-8') as f:
    for line in lines:
        if line.startswith('SET '):
            f.write('SET UTF-8\n')
        else:
            f.write(line)
" "%%F"
            )
            echo.
        ) else (
            echo Skipping dict-!CODE! (directory not found)
        )
    )
)

echo ========================================
echo  Conversion complete!
echo ========================================
echo.
echo Remember to update dictionaries.json release URLs if publishing a new version.
