@echo off
echo ========================================
echo Building SMD Executable
echo ========================================
echo.

echo Cleaning old build files...
if exist "build" rmdir /s /q "build"
if exist "dist" rmdir /s /q "dist"

echo.
echo Building executable...
echo This may take 5-10 minutes...
echo.

REM Suppress pkg_resources deprecation from PyInstaller/build deps so log stays clean
set PYTHONWARNINGS=ignore::UserWarning
python -m PyInstaller build_smd.spec

if errorlevel 1 (
    echo.
    echo ========================================
    echo BUILD FAILED!
    echo ========================================
    echo Make sure PyInstaller is installed: pip install pyinstaller
    pause
    exit /b 1
)

echo.
echo ========================================
echo BUILD SUCCESSFUL!
echo ========================================
echo.
echo Executable: dist\SMD.exe
echo.

if exist "dist\SMD.exe" (
    python -c "import os; size = os.path.getsize('dist/SMD.exe'); print(f'Size: {size / (1024*1024):.1f} MB')"
)

echo.
echo You can now run: dist\SMD.exe
echo Settings will be saved in: dist\settings.bin
echo.
pause
